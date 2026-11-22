from pathlib import Path
import csv

import numpy as np
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RESULTS_DIR = PROJECT_ROOT / "results"
OUTPUT_DIR = RESULTS_DIR / "figures"

SEEDS = [42, 123, 2026]
ROUNDS = 500


def load_curve(seed):

    file_path = (
        RESULTS_DIR /
        f"higgs_xgb_seed{seed}_curve.csv"
    )

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        rows = list(reader)

    if len(rows) != ROUNDS:
        raise ValueError(
            f"Seed {seed}: expected 500 rounds"
        )

    train_auc = [
        float(row["train_auc"]) for row in rows
    ]

    valid_auc = [
        float(row["valid_auc"]) for row in rows
    ]

    return train_auc, valid_auc


def main():

    train_curves = []
    valid_curves = []

    for seed in SEEDS:

        train, valid = load_curve(seed)

        train_curves.append(train)
        valid_curves.append(valid)

    train_curves = np.array(train_curves)
    valid_curves = np.array(valid_curves)

    train_mean = np.mean(train_curves, axis=0)
    valid_mean = np.mean(valid_curves, axis=0)

    train_std = np.std(
        train_curves, axis=0, ddof=1
    )

    valid_std = np.std(
        valid_curves, axis=0, ddof=1
    )

    rounds = np.arange(1, ROUNDS + 1)

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.plot(
        rounds,
        train_mean,
        label="Training AUC"
    )

    ax.fill_between(
        rounds,
        train_mean - train_std,
        train_mean + train_std,
        alpha=0.15
    )

    ax.plot(
        rounds,
        valid_mean,
        label="Validation AUC"
    )

    ax.fill_between(
        rounds,
        valid_mean - valid_std,
        valid_mean + valid_std,
        alpha=0.15
    )

    ax.set_xlabel("Boosting Rounds")
    ax.set_ylabel("AUC")

    ax.set_title(
        "Training and Validation AUC Across Boosting Rounds"
    )

    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        OUTPUT_DIR / "learning_curves_mean_auc.png"
    )

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print("Learning curve analysis completed.")
    print(f"Figure saved to: {output_path}")


if __name__ == "__main__":
    main()