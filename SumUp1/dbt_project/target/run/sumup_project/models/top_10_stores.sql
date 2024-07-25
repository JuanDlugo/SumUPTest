
  create view `SumUpTest1`.`top_10_stores__dbt_tmp`
    
    
  as (
    WITH store_transactions AS (
    SELECT
        s.name AS store_name,
        SUM(t.amount) AS total_amount
    FROM SumUpTest1.transactions t
    JOIN SumUpTest1.devices d ON t.device_id = d.id
    JOIN SumUpTest1.stores s ON d.store_id = s.id
    WHERE t.status = 'accepted'
    GROUP BY s.name
)
SELECT
    store_name,
    total_amount
FROM store_transactions
ORDER BY total_amount DESC
LIMIT 10
  );