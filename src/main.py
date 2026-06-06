from analysis import (
    load_data,
    basic_stats,
    high_risk_patients,
    age_group_analysis
)
from visualization import plots


def main():
    data = load_data("data/patients.csv")

    print("\n=== BASIC STATS ===")
    basic_stats(data)

    print("\n=== HIGH RISK PATIENTS ===")
    high_risk_patients(data)

    print("\n=== AGE GROUP ANALYSIS ===")
    age_group_analysis(data)

    plots(data)

if __name__ == "__main__":
    main()