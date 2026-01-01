# Digital Patient Sentinel 🛡️🏥

![Status](https://img.shields.io/badge/Status-Prototype-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Focus](https://img.shields.io/badge/Focus-GDPR%20%26%20Digital%20Health-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

![Project Banner](https://via.placeholder.com/1000x300.png?text=Digital+Patient+Sentinel:+EHR+%2B+IoT+Integration+Pipeline)

## 📖 Project Overview

**Digital Patient Sentinel** is an end-to-end Machine Learning pipeline designed to build **"Digital Patient Models"** for intensive care units (ICU). The system integrates static clinical data (EHR) with dynamic sensor signals (IoT) to predict acute critical risks, such as **Sepsis**.

> *"The goal is not just to train a model, but to engineer a trustworthy system that bridges the gap between raw data and clinical decision support."*

---

## 🎯 Key Features (Aligned with Industry Standards)

### 1. 🔒 Privacy & GDPR Compliance
Privacy is not an afterthought; it is baked into the ingestion phase (`src/privacy.py`).
* **Pseudo-Anonymization:** Automatically replaces raw patient IDs with SHA-256 cryptographic hashes.
* **Data Minimization:** Generalizes sensitive dates to prevent re-identification, ensuring ethical handling of patient data from step one.

### 2. 🧬 Biomedical Knowledge Integration
The model moves beyond "black-box" approaches by incorporating physiological domain knowledge:
* **Shock Index (SI):** Calculates `Heart Rate / Systolic BP` as an early indicator of hemodynamic instability.
* **Pulse Pressure:** Derived feature to monitor cardiovascular health.
* **Vitals Logic:** Automatic flagging of hypoxia and fever events based on sensor thresholds.

### 3. ⚙️ Modular Data Pipeline
Built as a structured Python package to simulate a production environment:
* **Ingestion:** Simulates heterogeneous data sources (Clinical demographics + High-frequency vitals).
* **Cleaning & Encoding:** Robust handling of categorical data and missing values.
* **Modeling:** Random Forest
