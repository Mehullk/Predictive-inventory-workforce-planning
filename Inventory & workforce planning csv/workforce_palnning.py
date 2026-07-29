"""
Simplified Workforce Planning Engine
Compatible with the uploaded workforce.csv
"""

from pathlib import Path
import argparse
import math
import pandas as pd


def ceil_int(x):
    return int(math.ceil(max(0, x)))


def load_workforce_csv(path: Path):
    df = pd.read_csv(path, encoding="utf-8-sig")
    df.columns = df.columns.str.strip()

    required = [
        "Date",
        "Product",
        "UnitsSold",
        "RequiredHeadcount",
        "StaffedHeadcount",
        "TotalLaborCost",
    ]

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df["Date"] = pd.to_datetime(df["Date"])
    return df


def plan(df):
    units_per_worker = (
        df["UnitsSold"] / df["RequiredHeadcount"].replace(0, 1)
    ).median()

    out = []

    for _, row in df.iterrows():
        required = ceil_int(row["UnitsSold"] / max(units_per_worker, 1))
        out.append({
            "Date": row["Date"],
            "Product": row["Product"],
            "ForecastUnits": row["UnitsSold"],
            "RequiredWorkers": required,
            "CurrentStaff": row["StaffedHeadcount"],
            "Gap": required - row["StaffedHeadcount"],
            "LaborCost": row["TotalLaborCost"],
        })

    return pd.DataFrame(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workforce",
        default="workforce_train.csv",
        help="Path to workforce_train.csv",
    )

    args = parser.parse_args()

    df = load_workforce_csv(Path(args.workforce))
    report = plan(df)

    Path("outputs").mkdir(exist_ok=True)
    report.to_csv("outputs/Workforce_Plan.csv", index=False)

    print("Done.")
    print("Report saved to outputs/Workforce_Plan.csv")


if __name__ == "__main__":
    main()
