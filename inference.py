from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="./feature_repo")


online_features = store.get_online_features(
    features=[
        "churn_features:tenure",
        "churn_features:MonthlyCharges",
        "churn_features:TotalCharges",
    ],
    entity_rows=[{"customerID": "7590-VHVEG"}],
).to_dict()

print(online_features)