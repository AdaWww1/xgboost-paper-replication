# Replication Plan

## 1. Objective

This project aims to reproduce the classification
experiment presented in Table 3 of the paper
"XGBoost: A Scalable Tree Boosting System"
(Chen and Guestrin, KDD 2016).

We focus on comparing XGBoost and scikit-learn
in terms of classification accuracy and
training efficiency on the Higgs-1M dataset.

The reproduction focuses on the experimental
evidence for XGBoost's efficiency rather than
reimplementing the algorithm from scratch.

## 2. Claims to Be Tested

**Claim 1: Predictive Performance**

XGBoost can achieve classification performance
comparable to scikit-learn's gradient boosting.

**Claim 2: Training Efficiency**

XGBoost can train substantially faster than
scikit-learn under comparable conditions.

**Original Reference:** Table 3, Section 6.3.

The original paper reports:

| Method | Test AUC | Time per Tree (sec) |
|---|---|---|
| XGBoost | 0.8304 | 0.6841 |
| scikit-learn | 0.8302 | 28.51 |

These values are reference results from the
original paper, not our experimental results.

Our main reproduction will focus on these
two methods. The R.gbm and column-subsampling
variants are outside the initial scope.

## 3. Experimental Setup

### Dataset

| Item | Planned Setting |
|---|---|
| Dataset | Higgs-1M |
| Source | UCI HIGGS |
| Task | Binary classification |
| Samples | 1,000,000 |
| Input features | 28 numerical features |
| Target | Binary label (0 or 1) |
| Data format | CSV |

The current download script extracts the first
1,000,000 rows from the original dataset.

This differs from the randomly selected subset
described in the paper and will be recorded
as a reproduction deviation.

### Data Splitting

The updated XGBoost training implementation uses:

- Training set: 70%
- Validation set: 15%
- Test set: 15%

For a dataset of 1,000,000 samples,
this corresponds to approximately:

- 700,000 training samples
- 150,000 validation samples
- 150,000 test samples

The validation set is used to monitor AUC
during the boosting process.

The held-out test set is used for final
performance evaluation.

The planned random seeds are 42, 123 and 2026.

For a fair comparison, XGBoost and the
scikit-learn baseline should use identical
data splits for each random seed.

### Model Configuration

| Parameter | Planned Setting | Current XGBoost Implementation |
|---|---|---|
| Dataset | Higgs-1M | Higgs-1M |
| Input features | 28 | 28 |
| Number of trees | 500 | 500 |
| Maximum tree depth | 8 | 8 |
| Learning rate | 0.1 | 0.1 |
| Objective | Binary classification | binary:logistic |
| Evaluation metric | AUC | AUC |
| Tree method | Exact greedy | Library default |
| Column sampling | 1.0 | Not explicitly configured |
| CPU threads | To be aligned | 8 |
| Random seeds | 42, 123, 2026 | Currently hard-coded to 123 |

The current implementation uses
the XGBoost Python training API.

The tree method is not explicitly specified
in the current training script.

The scikit-learn baseline is planned to use
sklearn.ensemble.GradientBoostingClassifier.

The baseline implementation and the final
experimental settings still require validation
before a fair model comparison can be made.

## 4. Environment and Reproducibility

Programming language: Python

Main library: XGBoost

Baseline library: scikit-learn

Supporting libraries:
NumPy, pandas, matplotlib

Environment information to record:

- Python version
- Exact package versions
- CPU model and available memory
- Operating system
- Random seeds
- Model hyperparameters

The project will use pinned package versions
to support reproducibility.

Hardware and software versions will be
recorded after environment validation.

## 5. Random Seeds

We plan to conduct the main experiment
using three random seeds:

- 42
- 123
- 2026

These are proposed reproduction seeds,
not seeds specified in the original paper.

For each model, we will report:

- Mean Test AUC
- Standard deviation of Test AUC
- Mean training time per tree
- Standard deviation of training time

All comparisons will use consistent
experimental settings.

### Current Implementation Status

Experimental result files and training logs
are available for seeds 42, 123 and 2026.

However, the committed training script
currently uses a fixed seed value of 123.

The seed should be made configurable
through a command-line argument or
a multi-seed experiment loop.

This is required to reproduce all three
runs without manually modifying the code.

The consistency of the existing result files
and training logs will be checked before
the results are used in the final analysis.

## 6. Evaluation Method

### Classification Performance

Test AUC will be used to evaluate binary
classification performance.

Predicted probabilities will be used to
calculate the ROC-AUC score.

### Training Efficiency

Training efficiency is measured using the
elapsed wall-clock training time.

Time per Tree is calculated as:

Time per Tree = Total Training Time / Number of Trees

The current XGBoost implementation measures
the execution time of xgb.train().

This includes the per-round evaluation of
training and validation AUC.

Dataset loading, data splitting, test-set
prediction and ROC plotting are excluded.

This timing definition must be considered
when comparing our results with the paper.

For a fair comparison with scikit-learn,
the timing protocol and computational
resources should be aligned or any
remaining differences clearly documented.

### Comparison with the Paper

A Paper vs. Ours table will be created after
the main experiments are completed.

Differences in hardware and software versions
must be considered when interpreting
training efficiency results.

Each reported result must be traceable to
the corresponding experiment log.

## 7. Experimental Procedure

The reproduction will follow these steps:

1. Prepare the Higgs-1M dataset.
2. Validate the Python environment.
3. Verify dataset loading and preprocessing.
4. Train the XGBoost model.
5. Train the scikit-learn baseline.
6. Calculate Test AUC and training time.
7. Repeat the experiments with three seeds.
8. Calculate mean and standard deviation.
9. Compare the results with Table 3.
10. Analyze differences from the paper.

A reduced-scale test will be conducted before
the full experiment to validate the pipeline.

Reduced-scale tests will not be presented as
full Higgs-1M reproduction results.

## 8. Deviations from the Original Paper

| Item | Original Setting | Current Implementation | Reason or Status |
|---|---|---|---|
| Dataset subset | Higgs-1M subset | First 1M HIGGS rows | Current extraction method |
| Data split | Exact procedure to be verified | 70/15/15 train/validation/test | Validation monitoring |
| Input features | 28 | 28 | Feature selection corrected |
| Tree method | Exact greedy | Library default | Explicit configuration pending |
| CPU threads | To be verified | 8 | Current training configuration |
| Software | 2016 implementations | Modern libraries | Software availability |
| Hardware | Original benchmark machine | To be documented | Hardware availability |
| Random seeds | Not specified for Table 3 | 42, 123, 2026 | Repeated evaluation |
| Training-time measurement | Paper benchmark protocol | Training with per-round AUC evaluation | Timing alignment pending |

The current results are preliminary
reproduction results.

The differences in data preparation,
tree construction methods, hardware,
software and timing protocols must be
considered when interpreting the results.

All remaining deviations will be reviewed
before the final model comparison.

## 9. Extension Experiment

We plan to investigate the effect of
maximum tree depth on classification
performance and training efficiency.

Proposed max_depth values:

4, 6, 8, 10

The following settings will remain fixed:

- Dataset
- Data splitting strategy
- Number of trees
- Learning rate
- Random seeds
- Evaluation metrics

Only maximum tree depth will be changed.

The extension will be conducted after
the main experiment is validated.

## 10. Starting Code and References

Official XGBoost repository:
https://github.com/dmlc/xgboost

Original paper:
https://arxiv.org/abs/1603.02754

Our project uses existing machine learning
libraries and develops its own scripts
for dataset preparation, training and
result analysis.

The exact installed library versions,
upstream source revisions where applicable,
licenses and modified files will be
documented as the implementation is finalized.
