from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="feature_repo")

entity_df = pd.DataFrame({
    "customerID": ["7590-VHVEG", "5575-GNVDE"],
    "event_timestamp": [pd.Timestamp.now()] * 2
})

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "churn_features:tenure",
        "churn_features:MonthlyCharges",
        "churn_features:TotalCharges",
    ],
).to_df()

print(training_df)