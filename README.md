# Wispour — IoT Irrigation Assistance System

A low-cost, infrastructure-independent soil moisture monitoring 
system for small-scale farming in Benin City, Edo State, Nigeria.

Built as a final year project at the University of East Anglia,
School of Computing Sciences, 2026.

## The Problem
Manual irrigation on small-scale farms in Benin City relies 
entirely on personal experience, leading to inefficient water 
use during the December to March dry season. Existing IoT 
irrigation systems assume cloud connectivity, making them 
unsuitable for rural environments with limited infrastructure.

## The Solution
A five-layer IoT system that classifies soil conditions as 
UNKNOWN, DRY, or WET using a capacitive sensor and consecutive 
confirmation mechanism, served via a locally hosted web 
interface with no external internet dependency.

## Hardware
- Raspberry Pi Pico 2W
- SEN0193 Capacitive Soil Moisture Sensor v2.0
- Red LED indicator (GPIO 15, 330Ω resistor)
- Total cost: approximately £18

## System Architecture
Five layers: Sensing → Processing → Communication → 
Application → Output

## How It Works
1. Sensor reads soil moisture every 10 seconds
2. 10 readings averaged to reduce noise
3. Average compared against calibrated threshold of 36,000
4. Five consecutive qualifying readings confirm state change
5. State served via HTTP to web interface at 192.168.4.1
6. Red LED activates on DRY confirmation

## Setup
1. Flash MicroPython to Pico 2W
2. Upload main.py via Thonny
3. Connect sensor to GPIO 28, LED to GPIO 15
4. Connect to WiFi network: SSID Soilmonitor, password 12345678
5. Open browser and navigate to 192.168.4.1

## Calibration
Run calibration.py to establish threshold for your soil type.
Current calibration: Dry 52,241 / Wet 19,926 / Threshold 36,000

## Results
All six test cases met. Calibration separation of 32,315 ADC 
units confirmed. No false state transitions observed during 
stable conditions.

## Future Development
- CSV data logging for longitudinal analysis
- Finding out behavioural patterns of soil and
- 

## Project Status
Active development. Inspection completed June 2026.
Continuing development toward ML extension.
