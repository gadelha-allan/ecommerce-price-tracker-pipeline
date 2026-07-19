WITH raw_data AS (
    SELECT * FROM {{ source('public', 'prices') }}
)
SELECT
    id AS product_id,
    title AS product_name,
    CAST(COALESCE(price, 0) AS NUMERIC) AS price,
    currency_id,
    permalink AS product_url,
    extracted_at
FROM raw_data

