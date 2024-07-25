
  create view `SumUpTest1`.`avg_transacted_amount__dbt_tmp`
    
    
  as (
    WITH store_typology_country AS (
    SELECT s.typology, s.country, AVG(t.amount) AS average_amount
    FROM SumUpTest1.transactions t
    JOIN SumUpTest1.devices d ON t.device_id = d.id
    JOIN SumUpTest1.stores s ON d.store_id = s.id
    WHERE t.status = 'accepted'
    GROUP BY s.typology, s.country
)
SELECT typology, country, average_amount
FROM store_typology_country
  );