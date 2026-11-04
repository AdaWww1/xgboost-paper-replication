# Replication Plan

## 1. Objective

The objective of this project is to reproduce
the classification experiment in the XGBoost paper.

We will compare XGBoost with scikit-learn
using the Higgs dataset.

## 2. Claims to Be Tested

**Claim 1:**

XGBoost can achieve competitive classification
performance while providing faster training
than scikit-learn.

**Original Reference:** Table 3

## 3. Experimental Setup

| Item | Planned Setting |
|---|---|
| Dataset | Higgs-1M |
| Task | Binary Classification |
| Models | XGBoost, scikit-learn |
| Number of Trees | 500 |
| Main Metric | Test AUC |
| Efficiency Metric | Time per Tree |

The exact data split and preprocessing procedure
will be verified before the main experiment.

## 4. Environment

- Programming Language: Python
- Main Library: XGBoost
- Baseline Library: scikit-learn
- Hardware: To be recorded
- Package Versions: To be recorded

## 5. Random Seeds

We plan to use at least three random seeds.

The same seeds will be used for comparable
experiments.

## 6. Experimental Procedure

1. Obtain and prepare the dataset.
2. Set up the experimental environment.
3. Train the XGBoost model.
4. Train the scikit-learn baseline.
5. Record AUC and training time.
6. Repeat the experiments using different seeds.
7. Compare our results with the original paper.

## 7. Extension

We plan to investigate the effect of maximum
tree depth on model performance and training time.

The other experimental settings will remain unchanged.

## 8. Deviations

All differences between the original paper
and our implementation will be recorded here.

| Item | Original Setting | Our Setting | Reason |
|---|---|---|---|
| Hardware | To be verified | To be recorded | - |
| Dataset scale | Higgs-1M | To be confirmed | - |

## 9. Starting Code

Official repository:
https://github.com/dmlc/xgboost

Starting commit and modified files:
To be recorded after checking the selected version.
