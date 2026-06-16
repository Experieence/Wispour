from machine import ADC, Pin
import network
import socket
import time

# --- Sensor Setup ---
sensor = ADC(Pin(28))          # Soil moisture sensor on GPIO 28 (ADC2)
green = Pin(15, Pin.OUT)         # green LED on GPIO
amber = Pin(10, Pin.OUT)
red = Pin(6, Pin.OUT)

amber.value(1)

# --- System Configuration ---
NUM_SAMPLES = 10               # Number of readings to average
THRESHOLD = 36000              # Calibrated threshold between dry and wet
SAMPLE_DELAY = 10              # Seconds between each sampling cycle

# --- State Variables ---
dry_count = 0
wet_count = 0
current_state = "UNKNOWN"

# --- Access Point Setup ---
def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="Soilmonitor", password="12345678")
    while not ap.active():
        pass
    print("Access Point Active")
    print("IP:", ap.ifconfig()[0])
    return ap.ifconfig()[0]

# --- Socket Setup ---
def open_socket(ip):
    addr = ('0.0.0.0', 80)
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    s.settimeout(1)
    return s

# --- Sensor Averaging ---
def get_average():
    # Takes NUM_SAMPLES readings and returns the integer average
    total = 0
    for _ in range(NUM_SAMPLES):
        total += sensor.read_u16()
        time.sleep(0.01)
    return total // NUM_SAMPLES

# --- State Machine ---
def update_state(avg):
    # Compares averaged reading against threshold
    # Requires 5 consecutive qualifying readings to confirm a state change
    global dry_count, wet_count, current_state
    if avg >= THRESHOLD:
        dry_count += 1
        wet_count = 0
        if dry_count >= 5:
            current_state = "DRY"
            red.value(1)       # red LED on when DRY confirmed
            green.value(0)
    else:
        wet_count += 1
        dry_count = 0
        if wet_count >= 5:
            current_state = "WET"
            red.value(0)       # red LED off when WET confirmed
            green.value(1)
# --- Web Interface ---
def webpage(state, avg):
    # Generates HTML page with colour coded state, moisture bar and timestamp
   
    # Background colour based on state
    colour = {
        "DRY": "#e74c3c",
        "WET": "#27ae60"
    }.get(state, "#95a5a6")
   
    # Advice message based on state
    advice = {
        "DRY": "Your soil needs watering.",
        "WET": "Your soil has enough moisture.",
        "UNKNOWN": "Reading soil conditions..."
    }.get(state, "")
   
    # Moisture percentage calculation
    # 52000 = dry baseline, 19900 = wet baseline from calibration
    moisture_pct = max(0, min(100, int((52000 - avg) / (52000 - 19900) * 100)))
   
    # Timestamp from system clock (time since startup)
    t = time.localtime()
    time_str = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
   
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta http-equiv='refresh' content='10'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <style>
    body {{
      font-family: 'Segoe UI', Arial, sans-serif;
      background: {colour};
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      color: white;
    }}
    .card {{
      background: rgba(255,255,255,0.15);
      border-radius: 20px;
      padding: 40px;
      max-width: 400px;
      width: 90%;
      box-shadow: 0 8px 32px rgba(0,0,0,0.2);
      text-align: center;
    }}
    h1 {{
      font-size: 2.5em;
      margin-bottom: 5px;
    }}
    h2 {{
      font-size: 1.4em;
      margin-bottom: 20px;
      opacity: 0.9;
    }}
    .advice {{
      font-size: 1.2em;
      margin-bottom: 25px;
    }}
    .bar-container {{
      background: rgba(255,255,255,0.2);
      border-radius: 10px;
      height: 20px;
      width: 100%;
      margin: 10px 0;
    }}
    .bar-fill {{
      background: white;
      border-radius: 10px;
      height: 20px;
      width: {moisture_pct}%;
      transition: width 0.5s;
    }}
    .moisture-label {{
      font-size: 1em;
      margin-bottom: 20px;
    }}
    .timestamp {{
      font-size: 0.8em;
      opacity: 0.7;
      margin-top: 15px;
    }}
    svg {{
      margin-bottom: 10px;
    }}
  </style>
</head>
<body>
  <div class="card">
    <svg width="40" height="55" viewBox="0 0 60 80">
      <path d="M30 5 C30 5 5 40 5 55 C5 68 16 75 30 75 C44 75 55 68 55 55 C55 40 30 5 30 5Z"
            fill="white" opacity="0.8"/>
    </svg>
    <h1>Soil Monitor</h1>
    <h2>CURRENT STATE: {state}</h2>
    <p class="advice">{advice}</p>
    <div class="bar-container">
      <div class="bar-fill"></div>
    </div>
    <p class="moisture-label">Moisture Level: {moisture_pct}%</p>
    <p class="timestamp">Last updated: {time_str}</p>
  </div>
</body>
</html>"""

# --- Main Loop ---
ip = start_ap()
connection = open_socket(ip)
try:
    while True:
        # Sample and average sensor readings
        avg = get_average()
        # Update system state based on averaged reading
        update_state(avg)
        # Generate web page with current state
        html = webpage(current_state, avg)
        # Print debug info to serial
        print("Avg:", avg, "State:", current_state)
        # Serve web page to connected client
        try:
            client = connection.accept()[0]
            request = client.recv(1024)
            client.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
            client.send(html)
            client.close()
        except OSError:
            pass
       
        # Wait before next sampling cycle
        time.sleep(SAMPLE_DELAY)
finally:
    print("System shutting down...")
    green.value(0)
    amber.value(0)
    red.value(0)
   
    try:
        connection.close()
    except:
        pass
