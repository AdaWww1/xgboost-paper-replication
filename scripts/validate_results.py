
"""Validate XGBoost experiment outputs and training logs."""

import csv
import math
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"
LOGS_DIR = PROJECT_ROOT / "logs"

EXPECTED_SEEDS = [42, 123, 2026]
EXPECTED_ROUNDS = 500


def read_csv(file_path):
    """Read a CSV file and return all records."""

    with file_path.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        return list(csv.DictReader(file))


def read_log(file_path):
    """Support UTF-8 and UTF-16 training logs."""

    content = file_path.read_bytes()

    if content.startswith((b"\xff\xfe", b"\xfe\xff")):
        return content.decode("utf-16")

    return content.decode("utf-8-sig")


def require(condition, message):
    """Raise an error when a validation check fails."""

    if not condition:
        raise ValueError(message)


def check_auc(value):
    """Check whether an AUC value is valid."""

    require(
        math.isfinite(value) and 0 <= value <= 1,
        f"Invalid AUC value: {value}"
    )


def validate_seed(seed):
    """Validate the results for one random seed."""

    result_path = (
        RESULTS_DIR / f"higgs_xgb_seed{seed}.csv"
    )

    curve_path = (
        RESULTS_DIR / f"higgs_xgb_seed{seed}_curve.csv"
    )

    log_path = (
        LOGS_DIR / f"higgs_xgb_seed{seed}.log"
    )

    roc_path = (
        RESULTS_DIR / f"roc_curve_seed{seed}.png"
    )

    for path in [
        result_path, curve_path, log_path, roc_path
    ]:
        require(
            path.is_file(),
            f"Missing file: {path.name}"
        )

    # Check the main result CSV.
    records = read_csv(result_path)

    require(
        len(records) == 1,
        "Expected exactly one result record"
    )

    row = records[0]

    require(
        row["method"] == "XGBoost",
        "Unexpected model name"
    )

    require(
        int(row["seed"]) == seed,
        "Seed does not match the file name"
    )

    require(
        int(row["num_rounds"]) == EXPECTED_ROUNDS,
        "Unexpected number of boosting rounds"
    )

    auc = float(row["test_auc"])
    tree_time = float(row["time_per_tree_sec"])

    check_auc(auc)

    require(
        math.isfinite(tree_time) and tree_time > 0,
        "Invalid training time"
    )

    # Check the training and validation AUC curve.
    curve = read_csv(curve_path)

    require(
        len(curve) == EXPECTED_ROUNDS,
        "Incomplete AUC curve"
    )

    for iteration, record in enumerate(curve, start=1):

        require(
            int(record["iteration"]) == iteration,
            "Missing or duplicated iteration"
        )

        check_auc(float(record["train_auc"]))
        check_auc(float(record["valid_auc"]))

    # Check the training log.
    log_text = read_log(log_path)

    require(
        "Traceback" not in log_text
        and "can't open file" not in log_text,
        "Execution error found in training log"
    )

    matches = re.findall(
        r"^\[(\d+)\]\s+train-auc:([\d.]+)"
        r"\s+valid-auc:([\d.]+)",
        log_text,
        re.MULTILINE
    )

    require(
        len(matches) == EXPECTED_ROUNDS,
        "Training log does not contain 500 rounds"
    )

    # Compare each logged AUC with its curve record.
    for iteration, match in enumerate(matches):

        log_iteration, train_auc, valid_auc = match

        require(
            int(log_iteration) == iteration,
            "Incorrect log iteration"
        )

        require(
            abs(
                float(train_auc)
                - float(curve[iteration]["train_auc"])
            ) <= 0.0000051,
            "Training AUC curve does not match log"
        )

        require(
            abs(
                float(valid_auc)
                - float(curve[iteration]["valid_auc"])
            ) <= 0.0000051,
            "Validation AUC curve does not match log"
        )

    # Compare final metrics with the log.
    logged_auc = re.findall(
        r"Test AUC:\s*([\d.]+)",
        log_text
    )

    logged_time = re.findall(
        r"Average time per tree:\s*([\d.]+)",
        log_text
    )

    require(
        len(logged_auc) == 1 and len(logged_time) == 1,
        "Missing or duplicated final metrics"
    )

    # Logs report final metrics to four decimals.
    require(
        abs(float(logged_auc[0]) - auc) <= 0.0000501,
        "Test AUC does not match the log"
    )

    require(
        abs(float(logged_time[0]) - tree_time)
        <= 0.0000501,
        "Training time does not match the log"
    )

    print(
        f"[PASS] Seed {seed}: "
        f"AUC={auc:.6f}, "
        f"Time/tree={tree_time:.6f}s, "
        f"Rounds={EXPECTED_ROUNDS}"
    )


def main():

    print("XGBoost Experiment Validation")
    print("-" * 50)

    passed = 0

    for seed in EXPECTED_SEEDS:
        try:
            validate_seed(seed)
            passed += 1

        except (
            OSError, ValueError, KeyError,
            TypeError, UnicodeError
        ) as error:

            print(f"[FAIL] Seed {seed}: {error}")

    print("-" * 50)

    print(
        f"Passed: {passed}/{len(EXPECTED_SEEDS)}"
    )

    if passed != len(EXPECTED_SEEDS):
        print("Validation failed.")
        return 1

    print("All expected result files passed validation.")

    print(
        "Note: file consistency checks do not "
        "replace independent experimental reruns."
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
