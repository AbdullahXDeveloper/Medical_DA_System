import matplotlib.pyplot as plt
import numpy as np

def plots(data):

    # Blood Pressure Histogram
    plt.hist(data[:,1])
    plt.title("Blood Pressure Distribution")
    plt.savefig("graphs/bp.png")
    plt.close()

    # Sugar vs Age Scatter
    plt.scatter(data[:,0], data[:,2])
    plt.title("Age vs Sugar Level")
    plt.savefig("graphs/sugar_age.png")
    plt.close()

    # Cholesterol Bar Chart
    plt.bar(range(len(data)), data[:,4])
    plt.title("Cholesterol Levels")
    plt.savefig("graphs/cholesterol.png")
    plt.close()