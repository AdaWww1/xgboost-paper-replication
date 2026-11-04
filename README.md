
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

The initial reproduction plan focuses on the classification experiment in Table 3 of the original paper.

- Dataset: Higgs-1M (planned)
- Models: XGBoost and scikit-learn
- Main metric: Test AUC
- Efficiency metric: Training time per tree
- Random seeds: At least three

The exact data split, preprocessing procedure and experimental parameters will be verified before running the main experiments.

## 5. Repository Structure

```text
xgboost-paper-replication/
├── .gitignore
├── README.md
└── docs/
    ├── paper_notes.md
    └── replication_plan.md
```

Additional directories for source code, scripts, configurations and experimental results will be added as the project develops.

## 6. Environment and Reproducibility

The project will use Python and the required machine learning libraries.

Python version, package versions, hardware information and random seeds will be recorded.

Installation instructions and experiment commands will be added after the environment and implementation are finalized.

## 7. Experimental Results

Experimental results will be compared with the original paper using the same evaluation metrics where possible.

Results will be reported as mean ± standard deviation across at least three random seeds.

All reported results will be traceable to experimental logs.

## 8. Project Status

Current progress:
- Paper analysis completed.
- Initial reproduction plan prepared.
- Experimental implementation and environment setup are in progress.

## 9. References

Chen, T., & Guestrin, C. (2016).
XGBoost: A Scalable Tree Boosting System.
Proceedings of KDD 2016.

https://arxiv.org/abs/1603.02754
