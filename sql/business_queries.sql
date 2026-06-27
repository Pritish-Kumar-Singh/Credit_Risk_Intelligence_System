USE credit_risk_db;

DESCRIBE credit_risk_raw;

-- we are checking here that how much balanced the dataset is and what is the percentage of defaulters and non defaulters. So that we can get an idea if this is an imbalanced dataset or not.
SELECT
    `default payment next month` AS default_flag,
    COUNT(*) AS customers,
    ROUND(COUNT(*) * 100.0 /(SELECT COUNT(*) FROM credit_risk_raw),2) AS percentage
FROM credit_risk_raw
GROUP BY `default payment next month`;
-- conclusion was that this is an imbalanced dataset as the defaulters(1) are 22% and non defaulters(0) are 78%

-- from this query it was concluded that gender has no huge effect as default rate of males(1) is 20% and of females(2) is 24%
SELECT
    SEX,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY SEX;

-- from this query it was clear that education is affecting the default rate and it should be kept in features while training the model, but education column has some wrong values like 0, 5 and 6
SELECT
    EDUCATION,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY EDUCATION
ORDER BY default_rate DESC;

-- marriage is not affecting that much as all the default rates are around 20-22%, but i has a wrong value like 0
SELECT
    MARRIAGE,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY MARRIAGE
ORDER BY default_rate DESC;


-- smaller age groups default less as compared to higher age groups such as 60s and 70s but their customer count is also less as compared to lower age groups
SELECT
    FLOOR(AGE / 10) * 10 AS age_group,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY age_group
ORDER BY age_group;


-- customers with less credit limit are defaulting more and customers with high limit are defaulting less(as expected because ofcourse they are trusted customers and the bank trusted them in the start due to their background)
SELECT
    CASE
        WHEN LIMIT_BAL < 50000 THEN 'LOW_LIMIT'
        WHEN LIMIT_BAL < 200000 THEN 'MEDIUM_LIMIT'
        ELSE 'HIGH_LIMIT'
    END AS limit_group,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY limit_group;


-- here we check the recent month payments status(september) and we get to know that payment history is extremely predictive.
SELECT
    PAY_0,
    COUNT(*) AS customers,
    ROUND(AVG(`default payment next month`) * 100,2) AS default_rate
FROM credit_risk_raw
GROUP BY PAY_0
ORDER BY PAY_0;
