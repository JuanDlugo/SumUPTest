
  create view `SumUpTest1`.`top_10_products__dbt_tmp`
    
    
  as (
    WITH product_sales AS (
    SELECT
        t.product_name,
        COUNT(*) AS total_sold
    FROM SumUpTest1.transactions t
    WHERE t.status = 'accepted'
    GROUP BY t.product_name
)
SELECT
    product_name,
    total_sold
FROM product_sales
ORDER BY total_sold DESC
LIMIT 10
  );