# 🌱 Wispour

An embedded IoT research project investigating soil moisture behaviour to support better irrigation decisions.

Wispour began as a simple threshold-based soil moisture monitoring system using a Raspberry Pi Pico 2 W. Through experimentation, I realised that representing soil using only binary "wet" and "dry" states does not accurately reflect real soil-water interactions.

The project is now evolving into a research-driven system that combines embedded systems, experimentation, automated data collection, and data analysis to develop a more representative model of soil behaviour.

> 🚧 **Project Status:** Active Development (Version 2 in Progress)

---

# 🎯 Project Goal

The goal of Wispour is to help plant owners and farmers make better irrigation decisions by understanding soil behaviour rather than relying solely on fixed moisture thresholds.

Instead of simply displaying whether soil is "wet" or "dry", future versions aim to model how soil changes over time, allowing more informative and useful irrigation recommendations.

---

# 📦 Technologies

- Raspberry Pi Pico 2 W
- MicroPython
- Python
- HTML
- CSS
- Wi-Fi Access Point
- SPI
- SD Card Logging *(Currently Developing)*
- Git & GitHub

---

# ✨ Version 1 Features

Current Version 1 includes:

- Soil moisture sensing
- ADC averaging to reduce sensor noise
- Binary wet/dry classification
- Wi-Fi Access Point
- Embedded web interface
- LED status indication
- Configurable sampling interval

---

# 🔬 Engineering Process

Rather than simply adding features, Wispour is developed through an iterative engineering process.

Each new version is based on evidence collected through controlled experiments.

```
Problem

↓

Prototype

↓

Experiment

↓

Collect Evidence

↓

Identify Limitations

↓

Improve System

↓

Repeat
```

This allows every improvement to be justified by experimental findings rather than assumptions.

---

# 🧪 Experiments

One of the main focuses of the project is understanding soil behaviour.

Current experiments investigate questions such as:

- How does the soil moisture sensor respond after water is added?
- How repeatable are sensor readings?
- How long does soil take to stabilise?
- What limitations exist within a binary wet/dry model?
- How can these observations improve future versions of the system?

Future experiments will be automated using SD card logging to enable long-duration data collection without manual supervision.

---

# 🧠 What I've Learned

This project has introduced me to multiple engineering disciplines while solving a real-world problem.

## Embedded Systems

- ADC sampling
- GPIO
- SPI communication
- Sensor integration
- SD card communication

## IoT

- Wi-Fi networking
- Embedded web servers
- Browser-based interfaces

## Software Engineering

- Modular Python development
- State machines
- System architecture
- Version control

## Experimental Design

- Controlled experiments
- Hypothesis-driven testing
- Repeatability
- Evidence-based development

## Data Collection & Analysis

- Sensor calibration
- Data logging
- Noise reduction through averaging
- Behavioural analysis
- Statistical thinking

## Systems Engineering

- Breaking complex systems into subsystems
- Identifying assumptions and limitations
- Iterative improvement
- Designing based on evidence

---

# 🚧 Current Development

Version 2 is currently under development.

Current work includes:

- Automated SD card data logging
- Battery-powered operation
- Long-duration controlled experiments
- Soil stabilisation analysis
- Behaviour-based soil state modelling
- Improving the overall system architecture

---

# 🚀 Roadmap

## ✅ Version 1

- Soil moisture monitoring
- Binary wet/dry classification
- Web interface
- Calibration

## 🚧 Version 2 (Current)

- SD card logging
- Automated experimentation
- Behavioural analysis
- Improved soil state modelling

## 🔮 Future Versions

- Statistical analysis
- Machine learning exploration
- Cloud connectivity
- Predictive irrigation recommendations
- Multi-sensor integration

---

# 💭 Philosophy

One of the biggest lessons from this project has been that building a working system is only one part of engineering.

Understanding why a system behaves the way it does requires observation, experimentation, documentation, and continual refinement.

Rather than treating Version 1 as a finished product, Wispour is being developed as an evolving engineering project where each experiment informs the design of the next iteration.

---

# 📈 Current Progress

This project is actively being developed.

The repository documents not only the implementation of the system, but also the engineering process, experiments, design decisions, and lessons learned throughout development.
