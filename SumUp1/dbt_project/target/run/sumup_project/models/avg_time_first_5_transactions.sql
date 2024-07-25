
  create view `SumUpTest1`.`avg_time_first_5_transactions__dbt_tmp`
    
    
  as (
    WITH store_transactions AS (
    SELECT
        d.store_id,
        t.happened_at,
        ROW_NUMBER() OVER(PARTITION BY d.store_id ORDER BY t.happened_at) AS txn_number
    FROM
        SumUpTest1.transactions t
    JOIN
        SumUpTest1.devices d
    ON
        t.device_id = d.id
    WHERE
        t.status = 'accepted'
),
store_first_5 AS (
    SELECT
        store_id,
        MAX(happened_at) AS fifth_txn_time,
        MIN(happened_at) AS first_txn_time
    FROM
        store_transactions
    WHERE
        txn_number <= 5
    GROUP BY
        store_id
),
store_durations AS (
    SELECT
        store_id,
        TIMESTAMPDIFF(DAY, first_txn_time, fifth_txn_time) AS duration_days
    FROM
        store_first_5
    WHERE
        EXISTS (
            SELECT
                1
            FROM
                store_transactions
            WHERE
                store_id = store_first_5.store_id
            HAVING
                COUNT(*) >= 5
        )
),
avg_time_per_store AS (
    SELECT
        store_id,
        AVG(duration_days) AS avg_time_days
    FROM
        store_durations
    GROUP BY
        store_id
)
SELECT
    'All Stores' AS store_id,
    AVG(avg_time_days) AS avg_time_days
FROM
    avg_time_per_store
  );