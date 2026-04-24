import streamlit as st
import pandas as pd
import snowflake.connector

st.set_page_config(page_title="EMCOR ServiceFlow Dashboard", page_icon="🏗️")
st.title("🏗️ Field Service Job Profitability")
st.markdown("Real-time margin analysis from Snowflake + dbt")

# Database Connection
def get_data():
    conn = snowflake.connector.connect(
        user='svc_field_pipeline',
        password='YourSecurePassword123!',
        account='thfprst-yyb61847',
        warehouse='compute_wh',
        database='service_db',
        schema='gold_service_ops',
        role='service_ops_svc'
    )
    query = """
SELECT 
    SITE_NAME, 
    REGION, 
    HOURS_LOGGED, 
    LABOR_MARGIN_REMAINING, 
    FINANCIAL_STATUS 
FROM FCT_JOB_PROFITABILITY
"""
    return pd.read_sql(query, conn)

df = get_data()

# KPI Metrics at the top
col1, col2 = st.columns(2)
col1.metric("Total Hours Logged", f"{df['HOURS_LOGGED'].sum():.1f}")
col2.metric("Avg Margin Remaining", f"${df['LABOR_MARGIN_REMAINING'].mean():,.2f}")

# The Chart
st.subheader("Profitability by Site")
st.bar_chart(data=df, x='SITE_NAME', y='LABOR_MARGIN_REMAINING')

# The Raw Data
st.subheader("Detailed Job Status")
st.dataframe(df.style.applymap(lambda x: 'color: red' if x == 'OVER BUDGET' else 'color: green', subset=['FINANCIAL_STATUS']))
