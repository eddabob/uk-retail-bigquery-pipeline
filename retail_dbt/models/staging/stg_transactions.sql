select
    trim(transaction_id) as transaction_id,
    trim(customer_id) as customer_id,
    cast(order_date as date) as order_date,
    initcap(trim(category)) as product_category,
    cast(amount_gbp as numeric) as amount_gbp
from {{ source('raw_retail', 'raw_transactions') }}
where transaction_id is not null
