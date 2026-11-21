
"""Synchronize XGBoost results for statistical analysis.

Source: per-seed CSV files in results/.
Destination: results/raw/xgb_preliminary_seed_results.csv.
"""

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

OUTPUT = (
    RESULTS / "raw" / "xgb_preliminary_seed_results.csv"
)

SEEDS = (42, 123, 2026)
EXPECTED_ROUNDS = 500

COLUMNS = [
    "experiment_type",
    "model",
    "seed",
    "test_auc",
    "train_time_sec",
    "max_depth",
    "n_estimators_actual",
    "notes",
]


def read_one_seed(seed):
    """Read and validate a single XGBoost result."""

    path = RESULTS / f"higgs_xgb_seed{seed}.csv"

    if not path.is_file():
        raise FileNotFoundError(
            f"Missing experiment result: {path}"
        )

    with path.open(
        "r",
        newline="",
        encoding="utf-8-sig",
    ) as file:
        rows = list(csv.DictReader(file))

    if len(rows) != 1:
        raise ValueError(
            f"{path.name}: expected exactly one data row"
        )

    record = rows[0]

    if record["method"].strip() != "XGBoost":
        raise ValueError(
            f"{path.name}: unexpected model name"
        )

    if int(record["seed"]) != seed:
        raise ValueError(
            f"{path.name}: seed mismatch"
        )

    rounds = int(record["num_rounds"])

    if rounds != EXPECTED_ROUNDS:
        raise ValueError(
            f"{path.name}: expected "
            f"{EXPECTED_ROUNDS} boosting rounds"
        )

    auc = float(record["test_auc"])
    time_per_tree = float(
        record["time_per_tree_sec"]
    )

    if not math.isfinite(auc) or not 0 <= auc <= 1:
        raise ValueError(
            f"{path.name}: invalid Test AUC"
        )

    if (
        not math.isfinite(time_per_tree)
        or time_per_tree <= 0
    ):
        raise ValueError(
            f"{path.name}: invalid training time"
        )

    # Total time is derived, not independently measured.
    derived_total_time = time_per_tree * rounds

    return {
        "experiment_type": "preliminary_main_reproduction",
        "model": "XGBoost",
        "seed": seed,
        "test_auc": auc,
        "train_time_sec": derived_total_time,
        "max_depth": 8,
        "n_estimators_actual": rounds,
        "notes": (
            "derived_from_time_per_tree_times_500;"
            f"source={path.name}"
        ),
    }


def main():
    """Generate the analysis input CSV."""

    records = [
        read_one_seed(seed)
        for seed in SEEDS
    ]

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    print(f"Updated analysis input: {OUTPUT}")
    print(f"Records: {len(records)}")

    for record in records:
        print(
            f"Seed {record['seed']}: "
            f"AUC={record['test_auc']:.6f}, "
            f"Derived total time="
            f"{record['train_time_sec']:.4f}s"
        )


if __name__ == "__main__":
    main()
