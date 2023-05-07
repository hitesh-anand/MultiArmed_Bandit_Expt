import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_repl = pd.read_csv("untimed_trialWise_data.csv", delimiter=",", header=0)
data_repl = data_repl.iloc[:,:].values

data_ext = pd.read_csv("trialWise_data.csv", delimiter=",", header=0)
data_ext = data_ext.iloc[:,:].values

conditions = {
    " IOWA": 0,
    " Equal Means": 1,
    " Low Var": 2,
    " High Var": 3
}

repl_values = [[0 for i in range(11)] for j in range(4)]
ext_values = [[0 for i in range(11)] for j in range(4)]
repl_count = [[0 for i in range(11)] for j in range(4)]
ext_count = [[0 for i in range(11)] for j in range(4)]

for ind, row in enumerate(data_repl):
    if row[2]==20:
        continue
    repl_values[conditions[row[1]]][int(row[2]/2)] += row[3]
    repl_count[conditions[row[1]]][int(row[2]/2)] += 1

x_vals = [2*i for i in range(10)]


for ind, row in enumerate(data_ext):
    ext_values[conditions[row[1]]][int(row[2]/2)] += row[3]
    ext_count[conditions[row[1]]][int(row[2]/2)] += 1


for i in range(4):
    y_vals_repl = []
    y_vals_ext = []

    for j in range(10):
        y_vals_repl.append(repl_values[i][j]/repl_count[i][j])
        y_vals_ext.append(ext_values[i][j]/ext_count[i][j])
    print(y_vals_ext)
    print(y_vals_repl)
    plt.subplot(2, 2, i+1)
    if i==0:
        plt.title("Average Repeat Choices after each Trial (in IOWA)")
    elif i==1:
        plt.title("Average Repeat Choices after each Trial (in Equal Means)")
    elif i==2:
        plt.title("Average Repeat Choices after each Trial (in Low Var)")
    elif i==3:
        plt.title("Average Repeat Choices after each Trial (in High Var)")
    plt.xlabel("Number of Trials")
    plt.ylabel("Repeat Choices")
    plt.grid()
    plt.plot(x_vals, y_vals_repl)
    plt.plot(x_vals, y_vals_ext)
    plt.xticks([2*i for i in range(10)])
    # plt.yticks([i for i in range(0, 1200, 200)])
    plt.tight_layout()
    # plt.legend(["without cognitive load", "with cognitive load"], loc ="lower right")

plt.show()
