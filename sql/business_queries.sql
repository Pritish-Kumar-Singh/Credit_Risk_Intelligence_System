USE credit_risk_db;

DESCRIBE credit_risk_raw;

SELECT
    `default payment next month` AS default_flag,
    COUNT(*) AS customers,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM credit_risk_raw),
        2
    ) AS percentage
FROM credit_risk_raw
GROUP BY `default payment next month`;

SELECT
    SEX,
    COUNT(*) AS customers,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY SEX;

SELECT
    EDUCATION,
    COUNT(*) AS customers,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY EDUCATION
ORDER BY default_rate DESC;

SELECT
    MARRIAGE,
    COUNT(*) AS customers,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY MARRIAGE
ORDER BY default_rate DESC;

SELECT
    FLOOR(AGE / 10) * 10 AS age_group,
    COUNT(*) AS customers,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY age_group
ORDER BY age_group;

SELECT
    CASE
        WHEN LIMIT_BAL < 50000 THEN 'LOW_LIMIT'
        WHEN LIMIT_BAL < 200000 THEN 'MEDIUM_LIMIT'
        ELSE 'HIGH_LIMIT'
    END AS limit_group,

    COUNT(*) AS customers,

    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate

FROM credit_risk_raw

GROUP BY limit_group;

SELECT
    PAY_0,
    COUNT(*) AS customers,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY PAY_0
ORDER BY PAY_0;

SELECT
    `default payment next month`,
    ROUND(AVG(BILL_AMT1),2) AS bill1,
    ROUND(AVG(BILL_AMT2),2) AS bill2,
    ROUND(AVG(BILL_AMT3),2) AS bill3
FROM credit_risk_raw
GROUP BY `default payment next month`;

SELECT
    `default payment next month`,
    ROUND(AVG(PAY_AMT1),2) AS pay1,
    ROUND(AVG(PAY_AMT2),2) AS pay2,
    ROUND(AVG(PAY_AMT3),2) AS pay3
FROM credit_risk_raw
GROUP BY `default payment next month`;

SELECT
    PAY_0,
    ROUND(
        AVG(`default payment next month`) * 100,
        2
    ) AS default_rate
FROM credit_risk_raw
GROUP BY PAY_0
ORDER BY default_rate DESC;