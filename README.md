# 🌱 Wispour

An embedded IoT research project investigating soil moisture behaviour to support better irrigation decisions. Wispour began as a threshold-based soil moisture monitor on a Raspberry Pi Pico 2 W. During calibration testing, it became clear that a binary "wet/dry" model doesn't reflect how soil actually behaves. See [Key Findings](#-key-findings) below. The project is now evolving into a research-driven system combining embedded systems, controlled experimentation, automated data logging, and data analysis to build a more representative model of soil behaviour.

**Status:** Active development — Version 2 in progress.

---

## 🎯 Goal

Help plant owners and small-scale farmers make better irrigation decisions by understanding soil behaviour, not just reacting to a fixed threshold. Future versions aim to model how soil moisture changes *over time*, rather than reporting a single wet/dry label.

---

## 🔍 Key Findings
---
WORK IN PROGRESS 

## 📦 Technologies

**Version 1 (built):**
- Raspberry Pi Pico 2 W · MicroPython
- ADC sampling
- Wi-Fi Access Point + embedded HTTP server
- HTML/CSS (served on-device)

**Version 2 (in progress):**
- SPI: SD card logging — [status: `[e.g. wiring complete, driver code in progress / basic writes working, not yet integrated into main loop]`]
- Battery-powered operation — [status: `[e.g. power budget calculated, not yet tested on hardware]`]

---

## ✨ Version 1 — Built and Tested

- Soil moisture sensing via capacitive sensor (ADC)
- 10-reading averaging to reduce sensor noise ([evidence](analysis/noise_reduction_summary.md) — raw ~200–500 unit variance reduced to ~100–200 units)
- Five-consecutive-reading confirmation to prevent state oscillation
- Binary wet/dry classification against a calibrated threshold (36,000 ADC units, [calibration data](datasets/calibration_runs_raw.txt))
- Self-hosted Wi-Fi Access Point + colour-coded web interface (no external server dependency)
- LED status indication
- Configurable sampling interval (10s demo / 5min field deployment)

Firmware: [`firmware/main.py`](firmware/main.py) 
Full write-up: [`docs/Final_Report.pdf`](docs/Final_Report.pdf)

---

## 🔬 Engineering Process

Each version is built on evidence from controlled experiments, not assumptions:

```
Problem → Prototype → Experiment → Collect Evidence
   ↑                                       ↓
   ←──────── Improve System ← Identify Limitations
```

Example of this loop in practice: an initial arbitrary threshold (16,500, used in the pre-hardware C simulation) was replaced by a placeholder (37,114) once running on real hardware, then replaced again by a calibrated value (36,000) once real dry/wet data was collected — and the comparison logic itself was corrected after calibration data showed dry soil produces *higher* ADC readings than wet soil, not lower. See [`firmware/archive/`](firmware/archive/) for the earlier versions.

---

## 🧪 Experiments

Current experiments investigate:

- How does the sensor respond immediately after water is added? → [TC4 transition test](datasets/TC4_threshold_transition_raw.txt)
- How repeatable are readings across separate calibration runs? → [calibration summary](analysis/calibration_summary.md) (dry avg varied by max 1,707 units across 3 runs; wet avg by only 128 units)
- How stable are readings over time in different soil states? → [TC2 stability test](datasets/TC2_stability_test_raw.txt)
- What are the limits of a binary wet/dry model? → [Key Finding](#-key-finding) above
- Does averaging meaningfully reduce noise? → [TC3 noise test](analysis/noise_reduction_summary.md)

Full experimental methodology: [`experiments/test_plan.md`](experiments/test_plan.md)

Version 2 experiments will use automated SD card logging to run long-duration tests (soil stabilisation over hours/days) without manual supervision not achievable with V1's REPL-based manual data collection.

---

## 🚧 Current Development (Version 2)

| Item | Status |
|---|---|
| SD card logging (SPI) | `[e.g. hardware wired, driver in progress]` |
| Battery-powered operation | `[status]` |
| Long-duration stabilisation experiments | `[blocked on SD logging / in progress]` |
| Behaviour-based soil state modelling (replacing binary classification) | `[design stage / early implementation]` |

---

## 🚀 Roadmap

**✅ Version 1** — soil moisture monitoring, binary classification, web interface, calibration

**🚧 Version 2 (current)** — SD card logging, automated long-duration experiments, behavioural/stabilisation analysis, improved soil state modelling

**🔮 Future** — statistical analysis of logged data, multi-sensor integration

---

## 🧠 Skills Demonstrated (with evidence)

| Area | Evidence |
|---|---|
| Embedded systems (ADC, GPIO, sensor integration) | [`firmware/main.py`](firmware/main.py) |
| IoT / networking | Self-hosted AP + HTTP server, no external dependency — [`firmware/main.py`](firmware/main.py) |
| Experimental design | Controlled, repeated-trial calibration (3 runs) — [`experiments/test_plan.md`](experiments/test_plan.md) |
| Data collection | Raw, timestamped logs preserved, not just summaries — [`datasets/`](datasets/) |
| Data analysis | Damp-soil drift finding, transient-reading identification — [Key Finding](#-key-finding) |
| Iterative engineering | Threshold and logic corrections across 3 firmware versions — [`firmware/archive/`](firmware/archive/) |

---

## 📈 Progress

This repository documents the implementation, the experiments behind each design decision, and the specific limitations found along the way. See [`docs/design_decisions.md`](docs/design_decisions.md) for the fuller reasoning behind architecture choices (e.g. why the system runs entirely on-device with no external server).
