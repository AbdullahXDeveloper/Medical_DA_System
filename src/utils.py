import numpy as np
import csv

def print_line():
    print("-" * 40)

def input_data():
    patients = []

    while True:
        age = int(input("Age: "))
        bp = int(input("Blood Pressure: "))
        sugar = int(input("Sugar Level: "))
        hr = int(input("Heart Rate: "))
        chol = int(input("Cholesterol: "))

        patients.append([age, bp, sugar, hr, chol])

        again = input("Add another patient? (y/n): ")

        with open("data/patients.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(patients)
   
        if again.lower() != "y":
            break

    print("Patient data saved successfully!")
    return np.array(patients)
