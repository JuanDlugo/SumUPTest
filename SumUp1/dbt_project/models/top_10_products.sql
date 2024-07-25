WITH product_sales AS (
    SELECT
        t.product_name,
        COUNT(*) AS total_sold
    FROM {{ source('sumup_source', 'transactions') }} t
    WHERE t.status = 'accepted'
    GROUP BY t.product_name
)
SELECT
    product_name,
    total_sold
FROM product_sales
ORDER BY total_sold DESC
LIMIT 10