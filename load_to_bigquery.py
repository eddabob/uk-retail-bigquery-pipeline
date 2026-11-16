import os
import pandas as pd
from google.cloud import bigquery

os.environ.setdefault("GOOGLE_APPLCIATION_CREDENTIALS", os.path.expanduser("~/.gcp/bq-key.json"))
PROJECT_ID = "project-dd910318-76d8-49a1-acb"
client = bigquery.Client(project=PROJECT_ID)

# Ensure you already created the 'retail_analytics' dataset 
# in BigQuery Studio under 'project-dd910318-76d8-49a1-acb' in region europe-west2
transactions = pd.DataFrame({
    "transaction_id": ["T001", "T002", "T003", "T004", "T005"],
    "customer_id": ["C101", "C102", "C101", "C103", "C102"],
    "order_date": pd.to_datetime(["2026-10-01", "2026-10-15", "2026-11-10", "2026-06-01", "2026-11-14"]),
    "category": ["  Electronics ", "Home", "electronics", "Clothing", "Home"],
    "amount_gbp": [299.99, 45.00, 89.50, 32.00, 110.00]
})

table_id = f"{PROJECT_ID}.retail_analytics.raw_transactions" #raw_transactions is the Table ID, retail_analytics is the Dataset ID
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
job = client.load_table_from_dataframe(transactions, table_id, job_config=job_config)
job.result()
print("SUCCESS: Loaded raw_transactions into BigQuery!")

