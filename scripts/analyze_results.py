import csv
import statistics
import argparse
from pathlib import Path
from collections import defaultdict


def read_experiments(file_path):
    """Read and validate experimental results."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {file_path}"
        )

    required_columns = [
        "experiment_type",
        "model",
        "seed",
        "test_auc",
        "train_time_sec"
    ]

    groups = defaultdict(
        lambda: {
            "auc": [],
            "train_time": [],
            "time_per_tree": [],
            "seeds": []
        }
    )

    with open(file_path, "r", encoding="utf-8-sig",
              newline="") as file:

        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The CSV file has no header.")

        missing = [
            col for col in required_columns
            if col not in reader.fieldnames
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        row_count = 0

        for row_number, row in enumerate(reader, start=2):

            if not any(
                value and value.strip()
                for value in row.values()
                if isinstance(value, str)
            ):
                continue

            row_count += 1

            try:
                experiment_type = row["experiment_type"].strip()
                model = row["model"].strip()
                seed = row["seed"].strip()

                if not experiment_type or not model or not seed:
                    raise ValueError("Empty experiment information")

                auc = float(row["test_auc"])
                train_time = float(row["train_time_sec"])

                if not 0 <= auc <= 1:
                    raise ValueError("AUC must be between 0 and 1")

                if train_time < 0:
                    raise ValueError("Training time cannot be negative")

                max_depth = (
                    row.get("max_depth", "").strip() or "N/A"
                )

                key = (experiment_type, model, max_depth)

                groups[key]["auc"].append(auc)
                groups[key]["train_time"].append(train_time)
                groups[key]["seeds"].append(seed)

                actual_trees = row.get(
                    "n_estimators_actual", ""
                ).strip()

                if actual_trees:
                    actual_trees = int(actual_trees)

                    if actual_trees <= 0:
                        raise ValueError(
                            "Actual number of trees must be positive"
                        )

                    groups[key]["time_per_tree"].append(
                        train_time / actual_trees
                    )

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid data at CSV row {row_number}: {error}"
                ) from error

    if row_count == 0:
        raise ValueError(
            "No experimental data found. "
            "Please provide actual experiment records."
        )

    return groups


def calculate_summary(groups):
    """Calculate statistics for each experimental group."""

    summary = []

    for (experiment_type, model, max_depth), data in groups.items():

        auc_values = data["auc"]
        time_values = data["train_time"]
        tree_times = data["time_per_tree"]

        mean_auc = statistics.mean(auc_values)

        std_auc = (
            statistics.stdev(auc_values)
            if len(auc_values) >= 2
            else ""
        )

        mean_time = statistics.mean(time_values)

        mean_tree_time = (
            statistics.mean(tree_times)
            if tree_times
            else ""
        )

        summary.append({
            "experiment_type": experiment_type,
            "model": model,
            "max_depth": max_depth,
            "runs": len(auc_values),
            "seeds": ";".join(data["seeds"]),
            "mean_test_auc": round(mean_auc, 6),
            "std_test_auc": (
                round(std_auc, 6)
                if std_auc != ""
                else ""
            ),
            "mean_train_time_sec": round(mean_time, 4),
            "mean_time_per_tree_sec": (
                round(mean_tree_time, 6)
                if mean_tree_time != ""
                else ""
            )
        })

    return summary


def save_summary(summary, output_path):
    """Save statistical results to a CSV file."""

    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    columns = [
        "experiment_type",
        "model",
        "max_depth",
        "runs",
        "seeds",
        "mean_test_auc",
        "std_test_auc",
        "mean_train_time_sec",
        "mean_time_per_tree_sec"
    ]

    with open(
        output_path,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=columns
        )

        writer.writeheader()
        writer.writerows(summary)

    print(f"\nSummary saved to: {output_path}")


def main():

    parser = argparse.ArgumentParser(
        description="Analyze XGBoost experimental results."
    )

    parser.add_argument(
        "input_csv",
        help="Path to the experimental results CSV file."
    )

    parser.add_argument(
        "--output",
        default="results/summary/model_summary.csv",
        help="Path to save the summary CSV."
    )

    args = parser.parse_args()

    try:
        groups = read_experiments(args.input_csv)

        summary = calculate_summary(groups)

        save_summary(summary, args.output)

        print("\nExperimental Summary")
        print("-" * 60)

        for item in summary:
            print(
                f"{item['model']} | "
                f"Depth: {item['max_depth']} | "
                f"Mean AUC: {item['mean_test_auc']} | "
                f"Std AUC: {item['std_test_auc']}"
            )

        print("\nAnalysis completed successfully.")

    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
