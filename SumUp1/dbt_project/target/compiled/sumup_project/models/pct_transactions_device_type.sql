WITH device_transactions AS (
    SELECT
        d.type AS device_type,
        COUNT(*) AS transaction_count
    FROM SumUpTest1.transactions t
    JOIN SumUpTest1.devices d ON t.device_id = d.id
    WHERE t.status = 'accepted'
    GROUP BY d.type
),
total_transactions AS (
    SELECT
        COUNT(*) AS total_count
    FROM SumUpTest1.transactions
    WHERE status = 'accepted'
)
SELECT
    dt.device_type,
    dt.transaction_count,
    (dt.transaction_count / tt.total_count) * 100 AS pct_transactions
FROM device_transactions dt, total_transactions tt