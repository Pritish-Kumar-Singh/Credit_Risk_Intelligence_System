# Credit Risk Intelligence System

## Overview

The Credit Risk Intelligence System is an end-to-end Machine Learning application designed to assess the probability of credit card default and generate actionable business recommendations.

The project combines:

* Machine Learning (XGBoost)
* FastAPI Backend
* Streamlit Frontend
* Explainability Layer
* Dockerized Deployment

Users can enter customer financial and repayment information and instantly receive:

* Default Probability
* Risk Classification
* Risk Drivers
* Personalized Recommendations
* Feature-Level Explanations

---

## Business Problem

Financial institutions need to identify customers who are likely to default on their credit obligations.

Manual assessment is slow and inconsistent.

This system automates risk assessment using historical customer behavior and repayment patterns.

---

## Architecture

Streamlit UI

↓

FastAPI API

↓

Data Validation

↓

Preprocessing

↓

Feature Engineering

↓

XGBoost Model

↓

Explainability Engine

↓

Risk Assessment & Recommendations

---

## Tech Stack

### Machine Learning

* XGBoost
* Scikit-Learn
* Imbalanced-Learn

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Deployment

* Docker
* Docker Hub

---

## Model Performance

| Metric    | Value   |
| --------- | ------- |
| Model     | XGBoost |
| ROC-AUC   | 0.7809  |
| Threshold | 0.55    |
| Features  | 36      |

---

## Features

### Risk Prediction

Predicts probability of customer default.

### Risk Classification

* LOW
* MEDIUM
* HIGH

### Explainability Layer

Displays business-friendly explanations for predictions.

### Recommendation Engine

Generates actionable credit risk recommendations.

### Downloadable Reports

Export prediction results as JSON.

### API Documentation

Swagger UI available through FastAPI.

---

## Project Structure

```text
Credit_Risk_Intelligence_System/

├── api/
├── app/
├── app/(CONTAINS SCREENSHOTS ABOUT THE PROJECT)
├── data/
│   ├── processed/
│   └── raw/
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
    └── 02_feature_engineering.ipynb
    └── 03_model_training.ipynb
│   └── 04_recommendation_engine.ipynb
├── src/
├── models/
│
├── reports/
│   ├── preprocessing_report.md
│   └── modeling_report.md
│
├── requirements.txt
├── requirements_prod.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## Running Locally

### Clone Repository

```bash
git clone <your-github-repo>
cd Credit_Risk_Intelligence_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start API

```bash
uvicorn api.main:app --reload
```

### Start Streamlit

```bash
streamlit run app/streamlit_app.py
```

---

## Running Using Docker

### Clone Repository

```bash
git clone <your-github-repo>
cd Credit_Risk_Intelligence_System
```

### Start Containers

```bash
docker compose up --build
```

### Open Applications

Streamlit:

http://localhost:8501

FastAPI:

http://localhost:8000

Swagger:

http://localhost:8000/docs

---

## Running Directly from Docker Hub

### Pull Images

```bash
docker pull pritish2docker/credit-risk-api:1.0

docker pull pritish2docker/credit-risk-streamlit:1.0
```

### Run API Container

```bash
docker run -d -p 8000:8000 --name credit-risk-api pritish2docker/credit-risk-api:1.0
```

### Run Streamlit Container

```bash
docker run -d -p 8501:8501 --name credit-risk-ui pritish2docker/credit-risk-streamlit:1.0
```

### Open Browser

http://localhost:8501

---

## Future Improvements

* Cloud Deployment (AWS/Azure/GCP)
* Database Integration
* User Authentication

---

## Author

Pritish Kumar Singh
Electrical Engineering | Data Science | Machine Learning

##  Connect With Me

* Email: [pritishsinghprf@gmail.com](mailto:pritishsinghprf@gmail.com)
* LinkedIn: www.linkedin.com/in/pritish1298

