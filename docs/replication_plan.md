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

The current implementation uses:

- Training set: 80%
- Test set: 20%
- Random state: 42

The final experimental procedure will be checked
against the original paper before conducting
the main reproduction.

The same train/test split must be used when
comparing XGBoost and scikit-learn.

### Model Configuration

| Parameter | Planned Setting |
|---|---|
| Models | XGBoost, scikit-learn |
| Number of trees | 500 |
| Maximum tree depth | 8 |
| Learning rate | 0.1 |
| XGBoost tree method | Exact greedy |
| Column sampling | 1.0 |
| Main metric | Test AUC |
| Efficiency metric | Time per Tree |

The number of trees, maximum depth, shrinkage
and exact greedy method follow the setting
described in the original paper.

The baseline is planned to use
sklearn.ensemble.GradientBoostingClassifier.

Other hyperparameters and implementation
differences will be documented when the
training scripts are finalized.

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

## 6. Evaluation Method

### Classification Performance

Test AUC will be used to evaluate binary
classification performance.

Predicted probabilities will be used to
calculate the ROC-AUC score.

### Training Efficiency

The training time will be measured separately
for each model.

Time per Tree is calculated as:

Time per Tree = Total Training Time / Number of Trees

Training time will exclude dataset downloading
and preprocessing whenever possible.

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

| Item | Original Setting | Our Setting | Reason |
|---|---|---|---|
| Dataset subset | Randomly selected 1M subset | First 1M rows | Current extraction method |
| Data split | Exact 1M split to be verified | 80/20 random split | Current implementation |
| Software | 2016 implementations | Modern pinned libraries | Availability |
| Hardware | Original benchmark machine | Local CPU, to be recorded | Resource availability |
| Random seeds | Not specified for Table 3 | 42, 123, 2026 | Statistical evaluation |

All deviations will be reviewed after
the final implementation is available.

The aim is to reproduce the paper's central
claims while transparently documenting any
differences in experimental conditions.

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
