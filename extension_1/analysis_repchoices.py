import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_untimed = pd.read_csv("untimed_trialWise_data.csv", delimiter=",", header=0)
data_untimed = data_untimed.iloc[:,:].values

data_timed = pd.read_csv("timed_trialWise_data.csv", delimiter=",", header=0)
data_timed = data_timed.iloc[:,:].values

conditions = {
    " IOWA": 0,
    " Equal Means": 1,
    " Low Var": 2,
    " High Var": 3
}

untimed_values = [[0 for i in range(11)] for j in range(4)]
timed_values = [[0 for i in range(11)] for j in range(4)]
untimed_count = [[0 for i in range(11)] for j in range(4)]
timed_count = [[0 for i in range(11)] for j in range(4)]

for ind, row in enumerate(data_untimed):
    untimed_values[conditions[row[1]]][int(row[2]/2)] += row[4]
    untimed_count[conditions[row[1]]][int(row[2]/2)] += 1

x_vals = [2*i for i in range(11)]


for ind, row in enumerate(data_timed):
    timed_values[conditions[row[1]]][int(row[2]/2)] += row[4]
    timed_count[conditions[row[1]]][int(row[2]/2)] += 1


for i in range(4):
    y_vals_untimed = []
    y_vals_timed = []

    for j in range(11):
        y_vals_untimed.append(untimed_values[i][j]/untimed_count[i][j])
        y_vals_timed.append(timed_values[i][j]/timed_count[i][j])
    plt.subplot(2, 2, i+1)
    if i==0:
        plt.title("Repeat Choices after each Trial (in IOWA)")
    elif i==1:
        plt.title("Repeat Choices after each Trial (in Equal Means)")
    elif i==2:
        plt.title("Repeat Choices after each Trial (in Low Var)")
    elif i==3:
        plt.title("Repeat Choices after each Trial (in High Var)")
    plt.xlabel("Number of Trials")
    plt.ylabel("Repeat Choices")
    plt.grid()
    plt.plot(x_vals, y_vals_untimed)
    plt.plot(x_vals, y_vals_timed)
    # plt.xticks([2*i for i in range(10)])
    # plt.yticks([i for i in range(0, 1000, 200)])
    plt.tight_layout()
    plt.legend(["untimed", "timed"], loc ="lower right")

plt.show()
