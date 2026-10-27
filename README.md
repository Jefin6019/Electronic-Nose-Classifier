# Electronic Nose (E-Nose) Classification Project

This repository contains a comprehensive data analysis pipeline for processing and classifying sensory responses recorded from an Electronic Nose (E-Nose) system. By parsing multi-sensor data patterns, the system automatically classifies environmental chemical profiles into distinct target conditions: clean air, different varieties of perfumes, and smoke exposure.

## 📸 Hardware System Setup
Below are reference images documenting the electronic nose system, sensor array configurations, and environmental test placements utilized during data collection:

<p align="center">
  <img src="images/WhatsApp Image 2026-10-27 at 8.31.49 (1).jpeg" width="31%" alt="E-Nose System Hardware Diagram">
  <img src="images/WhatsApp Image 2026-10-27 at 8.31.49.jpeg" width="31%" alt="Sensors Array Test Bench">
  <img src="images/WhatsApp Image 2026-10-27 at 8.31.48.jpeg" width="31%" alt="Environmental Testing Setup">
</p>

---

## 📁 Repository Structure
* **`Enose.py`**: Core Python data preprocessing, feature extraction, and machine learning classification loop.
* **`images/`**: Contains raw image logs documenting the physical electronic nose device components.
* **`clean air1_20260720_174914.xlsx`**: Raw sensor baseline response matrices collected under standard atmospheric conditions.
* **`perfume_1_20260713_122957.xlsx` / `perfume_20260713_090846.xlsx`**: Excel data logs documenting sensor arrays responding to active chemical perfume formulations.
* **`smoke_1_20260725_122520.xlsx` / `smoke_20260725_112958.xlsx`**: Air quality logs assessing sensor sensitivity drops during combustion exposure events.

---

## 🛠️ Installation & Prerequisites

To execute the data classification script, install the core data science libraries using your command-line terminal:

```bash
pip install pandas openpyxl scikit-learn matplotlib
```

---

## 🚀 Execution & Usage
Execute the analytical script to run the preprocessing pipelines and fit the classification model:

```bash
python Enose.py
```

## 📄 License
This project is open-source and available under the terms of the [MIT License](LICENSE).
