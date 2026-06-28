-- 1. Top NAV records
SELECT * FROM fact_nav ORDER BY nav DESC LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) FROM fact_nav GROUP BY amfi_code;

-- 3. Transactions by state
SELECT state, COUNT(*) FROM fact_transactions GROUP BY state;

-- 4. Total investment amount
SELECT SUM(amount_inr) FROM fact_transactions;

-- 5. SIP vs Lumpsum count
SELECT transaction_type, COUNT(*) FROM fact_transactions GROUP BY transaction_type;

-- 6. High expense funds
SELECT * FROM fact_performance WHERE expense_ratio_pct > 1;

-- 7. Top performing funds
SELECT * FROM fact_performance ORDER BY return_1yr_pct DESC LIMIT 5;

-- 8. Unique funds count
SELECT COUNT(DISTINCT amfi_code) FROM fact_nav;

-- 9. Transactions per city
SELECT city, COUNT(*) FROM fact_transactions GROUP BY city;

-- 10. Average expense ratio
SELECT AVG(expense_ratio_pct) FROM fact_performance;