
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
└── scripts/
    ├── download_higgs.py
    └── train_higgs.py
```

### Directory Description

- `docs/`: Paper analysis and experimental design.
- `scripts/`: Dataset preparation and model training.
- `requirements.txt`: Python package dependencies.
- `README.md`: Project overview and instructions.

The `data/`, `results/` and `logs/`
directories may be generated locally
during data preparation and experiments.

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

Experimental results will be compared with the original paper using the same evaluation metrics where possible.

Results will be reported as mean ± standard deviation across at least three random seeds.

All reported results will be traceable to experimental logs.

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

### Work in Progress

- Environment and dependency validation.
- Completing the model training pipeline.
- Implementing evaluation and result logging.
- Preparing repeated experiments using
  multiple random seeds.

The main experimental results have not
yet been finalized.

## 9. References

Chen, T., & Guestrin, C. (2016).
XGBoost: A Scalable Tree Boosting System.
Proceedings of KDD 2016.

https://arxiv.org/abs/1603.02754
