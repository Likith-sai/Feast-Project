import pandas as pd

df = pd.read_csv("Customer-Churn.csv")
df ["event_timestamp"] = pd.Timestamp.now()
df.to_parquet("feature_repo/data/churn_features.parquet")