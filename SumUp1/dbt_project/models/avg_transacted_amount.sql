WITH store_typology_country AS (
    SELECT s.typology, s.country, AVG(t.amount) AS average_amount
    FROM {{ source('sumup_source', 'transactions') }} t
    JOIN {{ source('sumup_source', 'devices') }} d ON t.device_id = d.id
    JOIN {{ source('sumup_source', 'stores') }} s ON d.store_id = s.id
    WHERE t.status = 'accepted'
    GROUP BY s.typology, s.country
)
SELECT typology, country, average_amount
FROM store_typology_country
