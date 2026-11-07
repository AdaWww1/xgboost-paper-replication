# Experimental Results Analysis Plan

## 1. Objective

The objective of this analysis is to evaluate the
experimental performance and training efficiency
of XGBoost and the scikit-learn baseline.

The analysis will focus on the following aspects:

- Classification performance.
- Training efficiency.
- Stability across different random seeds.
- The effect of hyperparameter changes.

## 2. Evaluation Metrics

The following metrics will be used:

| Metric | Description |
|---|---|
| Test AUC | Measures classification performance |
| Training Time | Total model training time |
| Training Time per Tree | Average training time per tree |

Training time per tree will be calculated as:

Training Time per Tree =
Total Training Time / Actual Number of Trees

## 3. Statistical Analysis

At least three random seeds will be used
for repeated experiments.

For each model, we will calculate:

- Mean performance.
- Standard deviation.
- Mean training time.

The results will be reported as:

Mean ± Standard Deviation

The sample standard deviation will be used.

## 4. Planned Visualizations

The following figures are planned:

### Figure 1. Model Performance Comparison

Compare the Test AUC of XGBoost and
the scikit-learn baseline.

### Figure 2. Training Efficiency Comparison

Compare the average training time per tree
between different models.

### Figure 3. Hyperparameter Sensitivity

Analyze the effect of maximum tree depth
(max_depth) on model performance and
training efficiency.

## 5. Extension Experiment Analysis

The extension experiment will investigate
the influence of maximum tree depth.

The following conditions will be controlled:

- Dataset and data split.
- Random seed.
- Number of estimators.
- Other model hyperparameters.

Only max_depth will be changed.

The relationship between tree depth,
Test AUC and training time will be analyzed.

## 6. Comparison with the Original Paper

Our experimental results will be compared
with the corresponding results reported
in the original XGBoost paper.

Differences in hardware, software environment,
dataset processing and experimental settings
will be considered when interpreting the results.

## 7. Data Quality and Reproducibility

All reported results must come from actual
experimental runs.

Each experiment should record:

- Model configuration.
- Random seed.
- Dataset split.
- Evaluation metrics.
- Training time.
- Software and hardware information.

Missing or incomplete experimental results
will not be included in the final statistical
comparison.

## 8. Pending Information

The following details will be confirmed
before the main analysis:

- Exact scikit-learn baseline model.
- Data splitting strategy.
- Final experimental parameters.
- Actual number of trees.
- Hardware and software environment.

## 9. Current Status

The analysis framework has been prepared.

Statistical analysis and visualizations
will be completed after the main experiments
are conducted.
