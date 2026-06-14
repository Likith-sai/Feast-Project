from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64
from datetime import timedelta

customer = Entity(name="customerID", join_keys=["customerID"])

churn_source = FileSource(
    path="data/churn_features.parquet",
    event_timestamp_column="event_timestamp",
)

churn_feature_view = FeatureView(
    name="churn_features",
    source=churn_source,
    entities=[customer],
    ttl=timedelta(days=365),
    schema=[
        Field(name="gender", dtype=Float64),
        Field(name="SeniorCitizen",dtype=Float64),
        Field(name="Partner",dtype=Float64),
        Field(name="Dependents",dtype=Float64),
        Field(name="tenure",dtype=Float64),
        Field(name="PhoneService",dtype=Float64),
        Field(name="MultipleLines",dtype=Float64),
        Field(name="InternetService",dtype=Float64),
        Field(name="OnlineSecurity",dtype=Float64),
        Field(name="OnlineBackup",dtype=Float64),
        Field(name="DeviceProtection",dtype=Float64),
        Field(name="TechSupport",dtype=Float64),
        Field(name="StreamingTV",dtype=Float64),
        Field(name="StreamingMovies",dtype=Float64),
        Field(name="Contract",dtype=Float64),
        Field(name="PaperlessBilling",dtype=Float64),
        Field(name="PaymentMethod",dtype=Float64),
        Field(name="MonthlyCharges",dtype=Float64),
        Field(name="TotalCharges",dtype=Float64),
        Field(name="Churn",dtype=Int64),
    ],
)