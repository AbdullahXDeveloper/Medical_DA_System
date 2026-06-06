import numpy as np

def load_data(file):
    data = np.genfromtxt(file, delimiter=",", skip_header=1)
    return data


def basic_stats(data):
    print("Mean Age:", np.mean(data[:,0]))
    print("Avg BP:", np.mean(data[:,1]))
    print("Avg Sugar:", np.mean(data[:,2]))
    print("Max Cholesterol:", np.max(data[:,4]))


def high_risk_patients(data):
    risk = data[
        (data[:,1] > 140) |
        (data[:,2] > 180) |
        (data[:,4] > 220)
    ]

    print("Total High Risk Patients:", len(risk))


def age_group_analysis(data):
    groups = {
        "18-30": data[(data[:,0] >= 18) & (data[:,0] <= 30)],
        "31-45": data[(data[:,0] >= 31) & (data[:,0] <= 45)],
        "46-60": data[(data[:,0] >= 46) & (data[:,0] <= 60)],
    }

    for k,v in groups.items():
        if len(v) > 0:
            print(f"{k} Avg Sugar:", np.mean(v[:,2]))