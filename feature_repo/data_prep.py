import pandas as pd

df = pd.read_csv("Customer-Churn.csv")
df ["event_timestamp"] = pd.Timestamp.now()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
df.to_parquet("data/churn_features.parquet")