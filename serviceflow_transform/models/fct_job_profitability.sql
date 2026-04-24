{{ config(materialized='table') }}

with stg_wo as (
    select * from {{ ref('stg_work_orders') }}
),

dim_sites as (
    select * from {{ ref('dim_job_sites') }}
),

final as (
    select
        wo.wo_id,
        s.site_name,
        s.region,
        wo.hours_logged,
        wo.mat_spend,
        s.budgeted_labor_amount as budget,
        (wo.hours_logged * 75) as labor_cost_actual,
        (s.budgeted_labor_amount - (wo.hours_logged * 75)) as labor_margin_remaining,
        -- Business Logic: Flagging risky jobs
        case 
            when (wo.hours_logged * 75) > s.budgeted_labor_amount then 'OVER BUDGET'
            when (wo.hours_logged * 75) > (s.budgeted_labor_amount * 0.8) then 'WARNING: AT RISK'
            else 'ON TRACK'
        end as financial_status
    from stg_wo wo
    left join dim_sites s on wo.site_id = s.site_id
)

select * from final
