# Paper Notes

## 1. Paper Information

**Title:** XGBoost: A Scalable Tree Boosting System

**Authors:** Tianqi Chen and Carlos Guestrin

**Conference:** KDD 2016

**Paper:** https://arxiv.org/abs/1603.02754

**Official Code:** https://github.com/dmlc/xgboost

## 2. Research Problem

The paper focuses on building a scalable and efficient
tree boosting system.

It aims to improve the training speed and scalability
of gradient tree boosting, especially when dealing
with large-scale and sparse datasets.

## 3. Main Contributions

1. A regularized learning objective to reduce model
   complexity and overfitting.

2. A weighted quantile sketch algorithm for
   approximate tree learning.

3. A sparsity-aware algorithm to handle missing
   values and sparse data.

4. System optimizations, including parallel learning,
   cache-aware access and out-of-core computation.

## 4. Experimental Datasets

The paper uses four datasets:

- Allstate: Insurance claim classification.
- Higgs Boson: Event classification.
- Yahoo LTRC: Learning to rank.
- Criteo: Click-through rate prediction.

## 5. Main Experiment of Our Project

We plan to focus on the classification experiment
in Table 3 of the original paper.

Dataset: Higgs-1M

Number of trees: 500

Methods:
- XGBoost
- scikit-learn

Evaluation metrics:
- Test AUC
- Training time per tree

## 6. Expected Reproduction Goal

We aim to examine whether XGBoost can achieve
similar classification performance while reducing
training time compared with scikit-learn.

## 7. References

Chen, T., & Guestrin, C. (2016).
XGBoost: A Scalable Tree Boosting System.
Proceedings of KDD 2016.
