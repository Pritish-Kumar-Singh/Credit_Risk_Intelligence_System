# SQL Business Analysis Report

## Project

**Credit Risk Intelligence System**

---

# Objective

The purpose of the SQL analysis phase was to understand customer default behavior before performing data preprocessing, feature engineering, and machine learning modeling.

The analysis focused on identifying:

* Customer segments with higher default risk
* Behavioral patterns associated with default
* Potential predictive features
* Business insights that can guide feature engineering and model development

---

# Dataset Summary

| Metric          | Value                      |
| --------------- | -------------------------- |
| Total Customers | 30,000                     |
| Features        | 24                         |
| Target Variable | Default Payment Next Month |
| Database        | credit_risk_db             |
| Table           | credit_risk_raw            |

---

# 1. Default Distribution Analysis

## Query Objective

Determine the percentage of customers who defaulted versus those who did not.

### Results

| Default Status | Customers | Percentage |
| -------------- | --------: | ---------: |
| No Default (0) |    23,364 |     77.88% |
| Default (1)    |     6,636 |     22.12% |

### Business Insight

The dataset is imbalanced but not severely.

Approximately 22% of customers defaulted on their next payment.

### Modeling Implication

* Classification metrics such as Precision, Recall, F1 Score, and ROC-AUC should be emphasized.
* Accuracy alone may be misleading.
* Class balancing techniques will be evaluated after baseline model performance is assessed.

---

# 2. Gender Risk Analysis

## Results

| Gender | Customers | Default Rate |
| ------ | --------: | -----------: |
| Male   |    11,888 |       24.17% |
| Female |    18,112 |       20.78% |

### Business Insight

Male customers exhibit a slightly higher default rate than female customers.

### Modeling Implication

Gender contains predictive information and should be retained as a feature.

---

# 3. Education Risk Analysis

## Results

| Education Level | Customers | Default Rate |
| --------------- | --------: | -----------: |
| High School     |     4,917 |       25.16% |
| University      |    14,030 |       23.73% |
| Graduate School |    10,585 |       19.23% |

### Business Insight

Customers with higher educational attainment tend to exhibit lower default risk.

### Modeling Implication

Education is a meaningful demographic predictor and should be retained.

---

# 4. Marriage Risk Analysis

## Results

| Marital Status | Customers | Default Rate |
| -------------- | --------: | -----------: |
| Other          |       323 |       26.01% |
| Married        |    13,659 |       23.47% |
| Single         |    15,964 |       20.93% |

### Business Insight

Marital status exhibits moderate predictive signal.

### Modeling Implication

Retain as a categorical feature.

---

# 5. Age Risk Analysis

## Results

| Age Group | Customers | Default Rate |
| --------- | --------: | -----------: |
| 20s       |     9,618 |       22.84% |
| 30s       |    11,238 |       20.25% |
| 40s       |     6,464 |       22.97% |
| 50s       |     2,341 |       24.86% |
| 60s       |       314 |       28.34% |
| 70s       |        25 |       28.00% |

### Business Insight

Default risk follows a non-linear relationship with age.

The lowest risk group is customers in their 30s, while older customers exhibit higher risk levels.

### Modeling Implication

Potential feature engineering opportunity:

* Age Groups
* Age Buckets
* Risk Segmentation by Age

---

# 6. Credit Limit Analysis

## Results

| Credit Limit Group | Customers | Default Rate |
| ------------------ | --------: | -----------: |
| Low Limit          |     4,311 |       36.07% |
| Medium Limit       |    14,539 |       23.34% |
| High Limit         |    11,150 |       15.13% |

### Business Insight

Credit limit is strongly associated with default behavior.

Customers with lower credit limits are significantly more likely to default.

### Modeling Implication

Credit limit is expected to be one of the strongest predictors in the dataset.

Potential feature engineering opportunities:

* Credit Limit Segments
* Credit Utilization Ratios
* Bill-to-Limit Ratios

---

# 7. Payment History Analysis

## Results

| PAY_0 Status | Customers | Default Rate |
| ------------ | --------: | -----------: |
| -2           |     2,759 |       13.23% |
| -1           |     5,686 |       16.78% |
| 0            |    14,737 |       12.81% |
| 1            |     3,688 |       33.95% |
| 2            |     2,667 |       69.14% |
| 3            |       322 |       75.78% |
| 4            |        76 |       68.42% |
| 5            |        26 |       50.00% |
| 6            |        11 |       54.55% |
| 7            |         9 |       77.78% |
| 8            |        19 |       57.89% |

### Business Insight

Payment history is the strongest risk indicator identified during SQL analysis.

As payment delays increase, default probability increases dramatically.

### Modeling Implication

PAY_0 and other payment status variables are expected to dominate model importance rankings.

Potential feature engineering opportunities:

* Average Payment Delay
* Maximum Delay
* Delay Frequency
* Recent Delay Indicators
* Chronic Delay Flags

---

# 8. Bill Amount Analysis

## Results

Average bill amounts were relatively similar between defaulters and non-defaulters.

### Business Insight

Raw bill amounts alone do not strongly separate risky and non-risky customers.

### Modeling Implication

Bill amounts may become more useful after feature engineering rather than as standalone variables.

---

# 9. Payment Amount Analysis

## Results

| Group       | PAY_AMT1 |
| ----------- | -------: |
| Default     |    3,397 |
| Non-Default |    6,307 |

### Business Insight

Customers who default tend to make significantly smaller payments.

### Modeling Implication

Payment behavior appears highly predictive.

Potential feature engineering opportunities:

* Payment Ratios
* Payment Consistency
* Average Payment Amount
* Payment-to-Bill Ratios

---

# Key Findings

## Strong Predictors

* PAY_0
* PAY_2
* PAY_3
* PAY_4
* PAY_5
* PAY_6
* LIMIT_BAL
* PAY_AMT1
* PAY_AMT2
* PAY_AMT3
* PAY_AMT4
* PAY_AMT5
* PAY_AMT6

## Moderate Predictors

* AGE
* EDUCATION
* MARRIAGE
* SEX

## Weak Standalone Predictors

* BILL_AMT1
* BILL_AMT2
* BILL_AMT3
* BILL_AMT4
* BILL_AMT5
* BILL_AMT6

These variables are expected to become more informative after feature engineering.

---

# SQL Phase Conclusion

The SQL analysis successfully identified the key business drivers of credit default risk.

The strongest signals originate from:

1. Historical payment behavior
2. Credit limit
3. Payment amounts

These findings will directly guide:

* Data preprocessing
* Feature engineering
* Feature selection
* Model development

Status: **SQL Business Analysis Completed**
