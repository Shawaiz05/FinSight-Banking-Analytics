-- ================================================
-- FinSight Banking Analytics
-- SQL Analysis Queries
-- Author: Mohammed Shawaiz Hussain
-- Database: PostgreSQL (Supabase)
-- Dataset: Credit Card Fraud Detection (215,945 rows)
-- ================================================


-- Query 1: Total transactions and fraud count
SELECT 
    COUNT(*) as total_transactions,
    SUM(CASE WHEN "Class" = 1 THEN 1 ELSE 0 END) as fraud_count,
    SUM(CASE WHEN "Class" = 0 THEN 1 ELSE 0 END) as normal_count,
    ROUND(SUM(CASE WHEN "Class" = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 4) as fraud_percentage
FROM transactions;


-- Query 2: Average transaction amount by fraud vs normal
SELECT 
    CASE WHEN "Class" = 1 THEN 'Fraud' ELSE 'Normal' END as transaction_type,
    ROUND(AVG("Amount_Scaled")::numeric, 4) as avg_amount,
    ROUND(MAX("Amount_Scaled")::numeric, 4) as max_amount,
    ROUND(MIN("Amount_Scaled")::numeric, 4) as min_amount,
    COUNT(*) as total
FROM transactions
GROUP BY "Class"
ORDER BY "Class" DESC;


-- Query 3: Top 10 highest fraud transactions
SELECT 
    id,
    "Amount_Scaled",
    "V1", "V2", "V3",
    "Class"
FROM transactions
WHERE "Class" = 1
ORDER BY "Amount_Scaled" DESC
LIMIT 10;


-- Query 4: Fraud distribution by amount range
SELECT
    CASE 
        WHEN "Amount_Scaled" < -0.5 THEN 'Low Amount'
        WHEN "Amount_Scaled" BETWEEN -0.5 AND 0.5 THEN 'Medium Amount'
        WHEN "Amount_Scaled" > 0.5 THEN 'High Amount'
    END as amount_range,
    COUNT(*) as total_transactions,
    SUM(CASE WHEN "Class" = 1 THEN 1 ELSE 0 END) as fraud_count
FROM transactions
GROUP BY amount_range
ORDER BY fraud_count DESC;


-- Query 5: Fraud rate summary statistics
SELECT
    ROUND(AVG(CASE WHEN "Class" = 1 THEN "Amount_Scaled" END)::numeric, 4) as avg_fraud_amount,
    ROUND(AVG(CASE WHEN "Class" = 0 THEN "Amount_Scaled" END)::numeric, 4) as avg_normal_amount,
    COUNT(CASE WHEN "Class" = 1 THEN 1 END) as total_fraud,
    COUNT(CASE WHEN "Class" = 0 THEN 1 END) as total_normal
FROM transactions;
