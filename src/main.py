from analysis import (
    load_data,
    basic_stats,
    high_risk_patients,
    age_group_analysis
)

from visualization import plots
from utils import input_data


def main():

    while True:

        print("\n========== Hospital Data Analytics System ==========")
        print("1. Add New Patient")
        print("2. Basic Statistics")
        print("3. High Risk Patients")
        print("4. Age Group Analysis")
        print("5. Generate Graphs")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            data = load_data("data/patients.csv")
            basic_stats(data)

        elif choice == "3":
            data = load_data("data/patients.csv")
            high_risk_patients(data)

        elif choice == "4":
            data = load_data("data/patients.csv")
            age_group_analysis(data)

        elif choice == "5":
            data = load_data("data/patients.csv")
            plots(data)
            print("Graphs generated successfully!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()