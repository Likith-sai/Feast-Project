# Feast Project

Simple example repository showing a small Feast-based feature repo and example training/inference scripts.

**Overview**

- **Purpose:** Demonstrate feature engineering and serving using Feast alongside simple training and inference workflows.
- **Contents:** feature store definitions, data prep, training, and inference example code.

**Repository Structure**

- [training.py](training.py): Training entrypoint for model development.
- [inference.py](inference.py): Example inference script that loads features and performs prediction.
- feature_repo/: Feast feature repository and helper scripts.
  - [feature_repo/feature_definitions.py](feature_repo/feature_definitions.py)
  - [feature_repo/data_prep.py](feature_repo/data_prep.py)
  - [feature_repo/churn_features.py](feature_repo/churn_features.py)
  - [feature_repo/feature_store.yaml](feature_repo/feature_store.yaml)
  - [feature_repo/test_workflow.py](feature_repo/test_workflow.py)

**Prerequisites**

- Python 3.9+ (recommended)
- Git
- (Optional) Docker if you want to run Feast locally on Docker

**Quick Setup**

1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install common dependencies (adjust as needed)

```bash
pip install --upgrade pip
pip install feast mlflow pandas scikit-learn pyarrow
```

3. (Optional) If you maintain a `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

**Configure Feast**

1. Open the feature repository config at [feature_repo/feature_store.yaml](feature_repo/feature_store.yaml) and adjust the `project` and `provider` settings for your environment.
2. Initialize or apply your feature repo using Feast CLI from the `feature_repo` folder:

```bash
cd feature_repo
feast init <feature_name>
feast apply
```

**Run training**

From the project root run the training script. `training.py` contains the model training workflow and may depend on features prepared in the feature repo. Need to change the entity_df and features parameters in get_historical_features() as per your requirements.

```bash
python training.py
```
## OUTPUT
```bash
python training.py 
   customerID                  event_timestamp  tenure  MonthlyCharges TotalCharges
0  7590-VHVEG 2026-06-14 13:34:38.482140+00:00       1           29.85        29.85
1  5575-GNVDE 2026-06-14 13:34:38.482140+00:00      34           56.95       1889.5
```

**Run Inference**

From the project root run the Inference script. `inference.py` contains the model training workflow and may depend on features prepared in the feature repo. 
If you are using any cloud for hosting the model/features then use below snippet in `inference.py` script.

```python
repo_config = RepoConfig(
    registry=RegistryConfig(path="/path/to/registry"),
    provider="<cloud provider name>",
)
store = FeatureStore(config=repo_config)
```


```bash
python inference.py
```
## OUTPUT
```bash
python inference.py 
{'customerID': ['7590-VHVEG'], 'MonthlyCharges': [None], 'TotalCharges': [None], 'tenure': [None]}
```