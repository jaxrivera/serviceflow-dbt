{{ config(materialized='view') }}

with raw_source as (
    select * from {{ source('internal_erp', 'fct_work_orders') }}
)

select
    work_order_id as wo_id,
    site_id,
    actual_labor_hours as hours_logged,
    material_cost as mat_spend,
    timestamp as recorded_at
from raw_source
