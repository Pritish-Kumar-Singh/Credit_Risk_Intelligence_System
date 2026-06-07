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
## Business Intelligence & SQL Analysis

Before building the machine learning model, extensive business analysis was performed using SQL to understand customer behavior, identify default patterns, and generate business insights.

The goal was to answer real-world business questions before moving to predictive modeling.

### SQL Analysis Objectives

The analysis focused on:

* Customer default behavior
* Payment delay patterns
* Credit utilization trends
* Repayment effectiveness
* Customer segmentation
* Risk concentration

### Key Business Questions Answered

#### 1. Which customer groups have the highest default rates?

#### 2. How do payment delays impact default risk?

#### 3. Does credit utilization influence risk?

#### 4. Are customers making sufficient repayments?

#### 5. Which customer segments are most risky?

### Key Findings

#### Payment History is the Strongest Risk Indicator

Customers with repeated repayment delays showed significantly higher default rates.

#### High Credit Utilization Increases Risk

Customers using a large percentage of their available credit were more likely to default.

#### Low Repayment Ratios Signal Financial Stress

Customers paying only a small portion of their monthly obligations demonstrated elevated risk levels.

#### Risk is Concentrated in Specific Customer Segments

Certain combinations of repayment behavior and credit utilization consistently produced higher default probabilities.

### Business Impact

The SQL analysis helped:

* Understand customer behavior before modeling
* Validate business assumptions
* Identify important risk factors
* Guide feature engineering decisions
* Improve model interpretability

### SQL Deliverables

The complete SQL analysis is documented in:

reports/sql_analysis.md

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

## Project Highlights

### Business Intelligence Layer

- SQL-driven risk analysis
- Customer segmentation
- Repayment behavior analysis
- Credit utilization analysis
- Business insight generation

### Machine Learning Layer

- XGBoost Risk Prediction
- Probability Scoring
- Risk Classification

### Explainability Layer

- Risk Drivers
- Feature Explanations
- Recommendation Engine

### Deployment Layer

- FastAPI Backend
- Streamlit Frontend
- Dockerized Architecture
- Docker Hub Distribution

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
│   └── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│   └── 04_recommendation_engine.ipynb
├── src/
├── models/
├── sql/
│
├── reports/
│   ├── preprocessing_report.md
│   └── modeling_report.md
│   └── sql_analysis.md
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

