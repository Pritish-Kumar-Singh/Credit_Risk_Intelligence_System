# Model Development Report

## Objective

Develop a machine learning model capable of predicting customer default risk using historical credit behavior.

---

## Problem Type

Binary Classification

Classes:

* 0 = No Default
* 1 = Default

---

## Modeling Workflow

1. Data Validation
2. Feature Engineering
3. Train-Test Split
4. Class Imbalance Handling
5. Model Training
6. Hyperparameter Optimization
7. Evaluation
8. Model Selection

---

## Class Imbalance Handling

Credit default datasets are naturally imbalanced.

To improve minority class detection:

* SMOTE oversampling was applied
* Evaluation focused on ROC-AUC and Recall

---

## Models Evaluated

### Logistic Regression

Advantages:

* Simple
* Interpretable
* Fast

Limitations:

* Struggles with complex nonlinear relationships

---

### Random Forest

Advantages:

* Robust
* Handles nonlinear interactions

Limitations:

* Larger models
* Slower inference

---

### CatBoost

Advantages:

* Strong predictive performance
* Handles complex relationships

Limitations:

* Higher computational cost

---

### XGBoost

Advantages:

* Excellent predictive performance
* Efficient inference
* Handles nonlinear patterns
* Strong regularization

Result:

Best overall model.

Selected for production deployment.

---

## Hyperparameter Optimization

Parameters explored:

* n_estimators
* learning_rate
* max_depth
* subsample
* colsample_bytree

The final configuration was selected based on validation ROC-AUC performance.

---

## Final Production Model

Model:

XGBoost

Features:

36

Decision Threshold:

0.55

ROC-AUC:

0.7809

---

## Explainability Layer

A business explanation engine was implemented to translate model outputs into human-readable insights.

Outputs include:

* Risk Drivers
* Feature Explanations
* Actionable Recommendations

This improves transparency and usability for business stakeholders.

---

## Production Architecture

Streamlit Frontend

↓

FastAPI Backend

↓

Validation Layer

↓

Preprocessing

↓

Feature Engineering

↓

XGBoost Model

↓

Recommendation Engine

↓

Prediction Response

---

## Conclusion

XGBoost achieved the strongest balance between predictive accuracy, interpretability, and deployment efficiency.

The final system delivers a complete production-style workflow capable of transforming raw customer information into actionable credit risk intelligence.
