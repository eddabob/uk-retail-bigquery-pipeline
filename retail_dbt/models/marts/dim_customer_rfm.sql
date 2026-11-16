with transactions as (
    select * from {{ ref('stg_transactions') }}
)

select
    customer_id,
    count(distinct transaction_id) as total_orders,
    sum(amount_gbp) as lifetime_spend_gbp,
    max(order_date) as last_order_date,
    date_diff(current_date(), max(order_date), day) as days_since_last_order,
    case
        when date_diff(current_date(), max(order_date), day) > 90 then true
        else false
    end as is_churn_risk
from transactions
group by customer_id
