WITH store_transactions AS (
    SELECT
        s.name AS store_name,
        SUM(t.amount) AS total_amount
    FROM {{ source('sumup_source', 'transactions') }} t
    JOIN {{ source('sumup_source', 'devices') }} d ON t.device_id = d.id
    JOIN {{ source('sumup_source', 'stores') }} s ON d.store_id = s.id
    WHERE t.status = 'accepted'
    GROUP BY s.name
)
SELECT
    store_name,
    total_amount
FROM store_transactions
ORDER BY total_amount DESC
LIMIT 10
