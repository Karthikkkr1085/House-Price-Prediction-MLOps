🏠 House Price Prediction MLOps Pipeline

An end-to-end MLOps project for predicting house prices using Machine Learning with a production-ready pipeline. This project demonstrates the complete lifecycle of an ML application, from data ingestion to deployment, monitoring, and data drift detection.

---

## 🚀 Features

- 📥 Data Ingestion
- ✅ Data Validation
- 🧹 Data Preprocessing
- ⚙️ Feature Engineering
- 🤖 Model Training
- 📊 Model Evaluation
- 📈 MLflow Experiment Tracking
- 🏪 Feast Feature Store
- 🌐 FastAPI REST API
- 🐳 Docker Containerization
- 📝 Prediction Logging
- 📡 Prometheus Monitoring
- 📉 Data Drift Detection using Kolmogorov–Smirnov (KS) Test

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3.x |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| API | FastAPI |
| Experiment Tracking | MLflow |
| Feature Store | Feast |
| Monitoring | Prometheus |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── api/
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── drift_detection/
├── feature_store/
├── logs/
├── models/
├── monitoring/
├── notebooks/
├── pipeline/
├── src/
├── tests/
├── Dockerfile
├── requirements.txt
├── README.md
└── main.py
```

---

## 🔄 Workflow

```
Dataset
    │
    ▼
Data Ingestion
    │
    ▼
Data Validation
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ├────────► MLflow
    │
    ├────────► Feast
    │
    ▼
FastAPI
    │
    ▼
Prediction API
    │
    ├────────► Prediction Logging
    ├────────► Prometheus Monitoring
    └────────► Data Drift Detection
```

---

## 📊 Machine Learning Pipeline

- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Model Serialization
- Prediction API
- Monitoring
- Drift Detection

---

## 📉 Data Drift Detection

The project monitors incoming prediction data and compares it with the reference training dataset using the **Kolmogorov–Smirnov (KS) Test**.

Generated Reports:

- `drift_report.csv`
- `drift_report.html`

---

## 🚀 Running the Project

### Clone Repository

```bash
git clone https://github.com/Karthikkkr1085/House-Price-Prediction-MLOps.git
cd House-Price-Prediction-MLOps
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Start FastAPI

```bash
uvicorn api.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📡 Prometheus Metrics

```
http://127.0.0.1:8000/metrics
```

---

## 📊 MLflow UI

```bash
mlflow ui
```

Open:

```
http://127.0.0.1:5000
```

---

## 🐳 Docker

Build

```bash
docker build -t house-price-prediction .
```

Run

```bash
docker run -p 8000:8000 house-price-prediction
```

---

## 📌 Future Enhancements

- Cloud Deployment
- Interactive Dashboard
- Automated Model Retraining

---

## 📷 Project Screenshots

Add screenshots of:

- FastAPI Swagger UI
- MLflow Dashboard
- Prometheus Metrics
- Prediction API
- Drift Report

---

## 👨‍💻 Author

**Karthik R**

GitHub: https://github.com/Karthikkkr1085

---

## ⭐ If you found this project useful, consider giving it a star!
