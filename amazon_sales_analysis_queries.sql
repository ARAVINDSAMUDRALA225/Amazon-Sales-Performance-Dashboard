-- Select the database
USE amazon_sales;

-- 1.Total number of orders in the dataset
SELECT COUNT(*) AS total_orders
FROM amazon_sales_cleaned;

-- 2️.Total revenue generated
SELECT SUM(amount) AS total_sales
FROM amazon_sales_cleaned;

-- 3️.Monthly sales trend (helps analyze business growth over time)
SELECT month, SUM(amount) AS month_sales
FROM amazon_sales_cleaned
GROUP BY month
ORDER BY month;

-- 4️.Top 10 states by sales (find strong business locations)
SELECT ship_state, SUM(amount) AS state_sales
FROM amazon_sales_cleaned
GROUP BY ship_state
ORDER BY state_sales DESC
LIMIT 10;

-- 5️.Category-wise sales performance
SELECT category, SUM(amount) AS category_sales
FROM amazon_sales_cleaned
GROUP BY category
ORDER BY category_sales DESC;

-- 6️.Fulfillment method analysis (which method performs better)
SELECT fulfilment, COUNT(*) AS total_orders, SUM(amount) AS total_sales
FROM amazon_sales_cleaned
GROUP BY fulfilment
ORDER BY total_sales DESC;

-- 7️.Order status distribution (delivered vs cancelled etc.)
SELECT status, COUNT(*) AS status_count
FROM amazon_sales_cleaned
GROUP BY status
ORDER BY status_count DESC;


