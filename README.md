# Feast Project

A small Feast-based example showing how a single schema definition prevents training-serving skew in a churn feature pipeline.

## Why this repository exists

This project demonstrates a common model deployment risk: training-serving skew when the feature schema used during training differs from the schema used during inference.

### Training-serving skew problem

- During training, the dataset includes `customerID` as the entity column plus feature values such as `tenure`, `MonthlyCharges`, and `TotalCharges`.
- During inference, if the requested feature schema does not exactly match the training schema, Feast may return a different set of columns or fill missing columns with `None`.
- A common workaround is to add a dummy column like `customerID` or `TotalCharges` to force the output schema to match, but this is brittle and error-prone.

In this repo, a mismatch between the entity definition and the served feature view can cause inference output to drop feature columns or return `None` for keys that are present during training.

## How Feast solves it

Feast solves training-serving skew by enforcing a single schema definition for the feature set.

- The feature definitions in `feature_repo/feature_definitions.py` and `feature_repo/feature_store.yaml` define one consistent set of features for both training and serving.
- The same feature store schema is used when calling `get_historical_features()` in `training.py` and `get_online_features()` in `inference.py`.
- This avoids the need for dummy columns or manual schema alignment between training and inference.

## Training vs Inference output

| Script | Example output | Notes |
|---|---|---|
| `python training.py` | `customerID`, `event_timestamp`, `tenure`, `MonthlyCharges`, `TotalCharges` | Historical feature join returns full training rows with expected schema |
| `python inference.py` | `customerID`, `MonthlyCharges`, `TotalCharges`, `tenure` | Online feature retrieval returns live values for the same schema |

### Example comparison

Training output example:

```text
customerID,event_timestamp,tenure,MonthlyCharges,TotalCharges
7590-VHVEG,2026-06-14 13:34:38.482140+00:00,1,29.85,29.85
5575-GNVDE,2026-06-14 13:34:38.482140+00:00,34,56.95,1889.5
```

Inference output example:

```text
{'customerID': ['7590-VHVEG'], 'MonthlyCharges': [None], 'TotalCharges': [None], 'tenure': [None]}
```

> Note: if inference returns `None` values for expected feature columns, it is usually a schema or entity-matching issue rather than a model problem.

## TotalCharges type fix

`TotalCharges` is often parsed as a string or object type in raw churn datasets. This repository includes a type fix so that `TotalCharges` is converted to numeric before features are materialized.

- This ensures the feature schema remains stable.
- It prevents downstream issues when models expect numeric input.

## Repository structure

- `training.py`: training workflow that uses Feast historical feature retrieval.
- `inference.py`: inference workflow that requests Feast online features.
- `feature_repo/feature_definitions.py`: feature definitions and schema.
- `feature_repo/data_prep.py`: raw data preparation and type conversions.
- `feature_repo/churn_features.py`: feature computation logic.
- `feature_repo/feature_store.yaml`: Feast feature store configuration.
- `feature_repo/test_workflow.py`: feature repo validation and workflow helper.

## Quick start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install feast mlflow pandas scikit-learn pyarrow
```

3. Apply the Feast feature repo:

```bash
cd feature_repo
feast apply
```

4. Run training:

```bash
python ../training.py
```

5. Run inference:

```bash
python ../inference.py
```
