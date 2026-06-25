--==========================================
-- Portfolio Analysis SQL Queries
-- Bond Analytics & Portfolio Risk Management
--==========================================

1. Total Market Value by Bond
SELECT
Bond_Name,
SUM(Market_Value) AS Total_Market_Value
FROM portfolio
GROUP BY Bond_Name
ORDER BY Total_Market_Value DESC;

2. Average Yield and Duration of Portfolio
SELECT
AVG(Yield) AS Average_Yield,
AVG(Duration) AS Average_Duration
FROM portfolio;

3. Highest Yield Bonds
SELECT
Bond_Name,
Yield,
Market_Value
FROM portfolio
ORDER BY Yield DESC
LIMIT 10;

 4. Bonds with Long Duration Risk
SELECT
Bond_Name,
Duration,
Yield
FROM portfolio
WHERE Duration > 5
ORDER BY Duration DESC;

5. Portfolio Allocation Percentage
SELECT
Bond_Name,
Market_Value,
ROUND(
(Market_Value * 100.0) /
(SELECT SUM(Market_Value) FROM portfolio),
2
) AS Allocation_Percentage
FROM portfolio
ORDER BY Allocation_Percentage DESC;

6. Bonds Trading Above Average Yield
SELECT
Bond_Name,
Yield
FROM portfolio
WHERE Yield >
(
SELECT AVG(Yield)
FROM portfolio
)
ORDER BY Yield DESC;

7. Maturity Distribution Analysis
SELECT
Maturity,
COUNT(*) AS Number_of_Bonds,
SUM(Market_Value) AS Total_Value
FROM bonds
GROUP BY Maturity
ORDER BY Maturity;

8. Top 5 Bonds by Market Value
SELECT
Bond_Name,
Market_Value
FROM portfolio
ORDER BY Market_Value DESC
LIMIT 5;

9. Portfolio Summary Statistics
SELECT
COUNT(*) AS Total_Holdings,
SUM(Market_Value) AS Portfolio_Value,
AVG(Yield) AS Avg_Yield,
AVG(Duration) AS Avg_Duration
FROM portfolio;

10. Yield Curve Summary
SELECT
AVG(Yield) AS Average_Yield,
MIN(Yield) AS Minimum_Yield,
MAX(Yield) AS Maximum_Yield
FROM yield_curve;
