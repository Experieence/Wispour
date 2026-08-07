from machine import ADC, Pin
import time

sensor = ADC(Pin(28))

NUM_READINGS = 20

def take_readings(label):
    readings = []
    
    print("\n---", label, "---")
    
    for i in range(NUM_READINGS):
        value = sensor.read_u16()
        readings.append(value)
        print(f"Reading {i+1}: {value}")
        time.sleep(0.2)
    
    avg = sum(readings) // len(readings)
    
    print(f"\n{label} AVERAGE: {avg}")
    print("----------------------")
    
    return avg


# --- MAIN ---
print("Calibration Test Starting...")

# Step 1: Dry
input("Place sensor in DRY condition and press Enter...")
dry_avg = take_readings("DRY")

# Step 2: Wet
input("Place sensor in WATER (cup) and press Enter...")
wet_avg = take_readings("WET")

# --- Calculate threshold ---
threshold = (dry_avg + wet_avg) // 2

print("\n=== CALIBRATION RESULT ===")
print("Dry Avg:", dry_avg)
print("Wet Avg:", wet_avg)
print("Suggested Threshold:", threshold)



