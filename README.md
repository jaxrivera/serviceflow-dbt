# 🏗️ ServiceFlow: Field Service Profitability Dashboard

ServiceFlow is a full-stack data engineering project designed to help field service managers track labor costs and job margins in real-time. By connecting **Snowflake** to **dbt** and **Streamlit**, the app transforms raw logs into a proactive financial management tool.

## 🚀 The Tech Stack
* **Warehouse:** Snowflake (Cloud Data Platform)
* **Transformation:** dbt (Data Build Tool) - handling modular SQL and business logic.
* **Visualization:** Streamlit (Python) - a reactive web dashboard.
* **Environment:** Python Virtual Environments (venv) & Git.

## 📊 Features
* **KPI Metrics:** Instant visibility into total hours logged and average margin remaining.
* **Risk Flagging:** Automated logic (via dbt) to categorize jobs as `ON TRACK`, `AT RISK`, or `OVER BUDGET`.
* **Data Integrity:** Implements a "Source-to-Sink" pipeline where the database schema acts as a data contract for the UI.

## 🛠️ How It Works
1. **Extraction:** Raw work order and site data reside in Snowflake.
2. **Transformation:** dbt cleans the data and calculates labor costs ($75/hr rate) and budget variances.
3. **Serving:** Streamlit queries the `GOLD` layer tables to display interactive charts.

## ⚙️ Installation & Usage
1. Clone the repo: `git clone https://github.com/YOUR_USER/serviceflow-dbt.git`
2. Activate venv: `source venv/bin/activate`
3. Run dbt: `dbt run --full-refresh` (inside the transform folder)
4. Launch App: `streamlit run app.py`
