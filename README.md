
# XGBoost Paper Replication

Replication study of "XGBoost: A Scalable Tree Boosting System" for the MIAE01 course project.

## 1. Project Overview

This project aims to reproduce selected experiments from the original XGBoost paper.

The main focus is the classification experiment in the original paper. We plan to compare XGBoost with a scikit-learn baseline and analyze their classification performance and training efficiency.

## 2. Original Paper

**Title:** XGBoost: A Scalable Tree Boosting System

**Authors:** Tianqi Chen and Carlos Guestrin

**Conference:** KDD 2016

**Paper:** https://arxiv.org/abs/1603.02754

## 3. Starting Code

**Official Repository:** https://github.com/dmlc/xgboost

The exact starting commit, license information and modified files will be documented before the experiments.

## 4. Reproduction Scope

The project focuses on the classification
experiment in Section 6.3 and Table 3 of
the original XGBoost paper.

### Main Reproduction

- Dataset: Higgs-1M
- Task: Binary classification
- Models: XGBoost and scikit-learn
- Number of trees: 500
- Maximum tree depth: 8
- Learning rate: 0.1
- Main metric: Test AUC
- Efficiency metric: Time per Tree

We aim to investigate whether XGBoost can
achieve comparable classification accuracy
while offering higher training efficiency.

### Statistical Evaluation

We plan to use three random seeds:
42, 123 and 2026.

Results will be reported using the mean
and standard deviation across repeated runs.

### Extension

An additional experiment will investigate
the effect of maximum tree depth on
classification performance and training time.

For the detailed experimental protocol, see
[Replication Plan](docs/replication_plan.md).

## 5. Repository Structure

```text
xgboost-paper-replication/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/
│   ├── paper_notes.md
│   └── replication_plan.md
├── logs/
│   ├── higgs_xgb_seed42.log
│   ├── higgs_xgb_seed123.log
│   └── higgs_xgb_seed2026.log
├── results/
│   ├── higgs_xgb_seed42.csv
│   ├── higgs_xgb_seed123.csv
│   └── higgs_xgb_seed2026.csv
└── scripts/
    ├── download_higgs.py
    └── train_higgs.py
```

### Directory Description

- `docs/`: Paper analysis and experimental design.
- `scripts/`: Dataset preparation and model training.
- `requirements.txt`: Python package dependencies.
- `README.md`: Project overview and instructions.

The `data/` directory is created locally
during dataset preparation and is excluded
from GitHub.

The `results/` and `logs/` directories
contain preliminary experiment outputs
committed for reproducibility and analysis.

Additional analysis scripts and result files
will be added as the project progresses.

## 6. Environment and Reproducibility

The project uses Python and existing
machine learning libraries.

Main dependencies include:

- XGBoost
- scikit-learn
- pandas
- NumPy
- matplotlib

### Dataset Preparation

The dataset is obtained from the
UCI HIGGS dataset repository.

The existing download script can be invoked
from the project root directory:

```bash
python scripts/download_higgs.py
```

The script is designed to extract
1,000,000 samples and save them to:

`data/HIGGS_1M.csv`

The current extraction method selects the
first 1,000,000 rows of the original HIGGS
dataset rather than a randomly sampled subset.

This difference from the original paper
is documented in the replication plan.

The downloaded dataset should not be
committed to GitHub because of its size.

### Training Environment

The training pipeline is currently
under development.

The dependency file and training script
still require validation before the main
experiment can be reproduced reliably.

Once the implementation has been tested,
this section will be updated with:

- Verified Python and library versions
- Installation commands
- Training commands
- Expected output files
- Actual runtime information

## 7. Experimental Results

### Preliminary XGBoost Results

The initial XGBoost training implementation
has been added to the repository.

Three preliminary result files have been
uploaded for random seeds 42, 123 and 2026.

| Seed | Test AUC | Time per Tree (s) |
|---|---|---|
| 42 | 0.82278 | 0.04274 |
| 123 | 0.82230 | 0.03324 |
| 2026 | 0.82218 | 0.03317 |

These results are preliminary and require
further reproducibility verification.

The committed training script currently
uses a fixed random seed and 27 features
instead of the expected 28 features.

The log for seed 42 also requires correction.

Therefore, the results are not yet treated
as validated three-seed reproduction results.

### Remaining Work

- Verify all three random-seed experiments.
- Correct the feature selection.
- Complete the scikit-learn baseline.
- Calculate mean and standard deviation.
- Compare the validated results with Table 3.
- Analyze differences from the original paper.

The final results will be updated after
the experiment pipeline has been validated.

## 8. Project Status

The project has completed its initial
paper analysis and experiment planning.

### Current Progress

- Reviewed the original XGBoost paper.
- Selected Table 3 as the reproduction target.
- Defined the primary evaluation metrics.
- Developed the initial experimental protocol.
- Added the dataset preparation script.
- Created the initial training script.
- Established the repository structure.
- Completed an initial XGBoost training run.
- Uploaded preliminary XGBoost results
  for three random seeds.
- Identified reproducibility issues
  requiring further validation.

### Work in Progress

- Correcting the feature selection to use
  all 28 numerical features.
- Improving random seed configuration
  and experiment reproducibility.
- Validating the three preliminary
  XGBoost result files and logs.
- Completing the scikit-learn baseline.
- Implementing statistical result analysis.
- Preparing the extension experiment.

The main experimental results have not
yet been finalized.

## 9. References

Chen, T., & Guestrin, C. (2016).
XGBoost: A Scalable Tree Boosting System.
Proceedings of KDD 2016.

https://arxiv.org/abs/1603.02754
