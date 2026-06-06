import numpy as np

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

        if again.lower() != "y":
            break

    return np.array(patients)
