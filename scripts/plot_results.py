
import csv
from pathlib import Path

import matplotlib.pyplot as plt


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = (
    PROJECT_ROOT
    / "results"
    / "raw"
    / "xgb_preliminary_seed_results.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "results" / "figures"


def load_results(file_path):
    """Load preliminary experimental results from CSV."""

    required_columns = [
        "seed",
        "test_auc",
        "train_time_sec",
        "n_estimators_actual"
    ]

    results = []

    with open(
        file_path,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file has no header.")

        missing = [
            column for column in required_columns
            if column not in reader.fieldnames
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        for row in reader:
            seed = int(row["seed"])
            auc = float(row["test_auc"])
            train_time = float(row["train_time_sec"])
            n_trees = int(row["n_estimators_actual"])

            if not 0 <= auc <= 1:
                raise ValueError("Invalid AUC value.")

            if train_time < 0 or n_trees <= 0:
                raise ValueError("Invalid training time or tree count.")

            time_per_tree = train_time / n_trees

            results.append({
                "seed": seed,
                "auc": auc,
                "time_per_tree": time_per_tree
            })

    if not results:
        raise ValueError("No experimental results found.")

    return sorted(results, key=lambda item: item["seed"])


def plot_auc(results, output_dir):
    """Visualize Test AUC across different random seeds."""

    seeds = [str(item["seed"]) for item in results]
    auc_values = [item["auc"] for item in results]

    fig, ax = plt.subplots(figsize=(8, 5))

    positions = range(len(seeds))

    ax.scatter(
        positions,
        auc_values,
        s=90
    )

    for x, value in zip(positions, auc_values):
        ax.annotate(
            f"{value:.6f}",
            (x, value),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center"
        )

    value_range = max(auc_values) - min(auc_values)
    margin = max(value_range * 0.5, 0.0002)

    ax.set_ylim(
        min(auc_values) - margin,
        max(auc_values) + margin
    )

    ax.set_xticks(list(positions))
    ax.set_xticklabels(seeds)

    ax.set_xlabel("Random Seed")
    ax.set_ylabel("Test AUC")
    ax.set_title("Test AUC Across Random Seeds")

    ax.text(
        0.02,
        0.02,
        "Note: The y-axis is truncated to show small differences.",
        transform=ax.transAxes,
        fontsize=8
    )

    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    output_path = output_dir / "test_auc_by_seed.png"

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"AUC figure saved to: {output_path}")


def plot_training_time(results, output_dir):
    """Visualize average training time per tree."""

    seeds = [str(item["seed"]) for item in results]

    times = [
        item["time_per_tree"]
        for item in results
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(
        seeds,
        times,
        width=0.55
    )

    for bar, value in zip(bars, times):
        ax.annotate(
            f"{value:.6f}",
            (
                bar.get_x() + bar.get_width() / 2,
                bar.get_height()
            ),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center"
        )

    ax.set_xlabel("Random Seed")
    ax.set_ylabel("Time per Tree (seconds)")
    ax.set_title("Training Time per Tree Across Random Seeds")

    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    output_path = (
        output_dir / "training_time_per_tree_by_seed.png"
    )

    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Training time figure saved to: {output_path}")


def main():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    results = load_results(INPUT_FILE)

    print(f"Loaded {len(results)} experimental records.")

    plot_auc(results, OUTPUT_DIR)

    plot_training_time(results, OUTPUT_DIR)

    print("\nVisualization completed successfully.")


if __name__ == "__main__":
    main()
