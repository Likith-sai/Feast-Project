from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64, String
from feast.value_type import ValueType
from datetime import timedelta

customer = Entity(name="customerID", join_keys=["customerID"], value_type=ValueType.STRING)

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
        Field(name="gender", dtype=String),
        Field(name="SeniorCitizen",dtype=Int64),
        Field(name="Partner",dtype=String),
        Field(name="Dependents",dtype=String),
        Field(name="tenure",dtype=Int64),
        Field(name="PhoneService",dtype=String),
        Field(name="MultipleLines",dtype=String),
        Field(name="InternetService",dtype=String),
        Field(name="OnlineSecurity",dtype=String),
        Field(name="OnlineBackup",dtype=String),
        Field(name="DeviceProtection",dtype=String),
        Field(name="TechSupport",dtype=String),
        Field(name="StreamingTV",dtype=String),
        Field(name="StreamingMovies",dtype=String),
        Field(name="Contract",dtype=String),
        Field(name="PaperlessBilling",dtype=String),
        Field(name="PaymentMethod",dtype=String),
        Field(name="MonthlyCharges",dtype=Float64),
        Field(name="TotalCharges",dtype=Float64),
        Field(name="Churn",dtype=String),
    ],
)