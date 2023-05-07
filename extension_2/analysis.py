import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_untimed = pd.read_csv("trialWise_data.csv", delimiter=",", header=0)
# print(data_untimed)
data_untimed = data_untimed.iloc[:, :].values

# print(data_untimed)
conditions = {
    " IOWA": 0,
    " Equal Means": 1,
    " Low Var": 2,
    " High Var": 3
}

values = [[0 for i in range(10)] for j in range(4)]
count = [[0 for i in range(10)] for j in range(4)]

# exit(0)
for ind, row in enumerate(data_untimed):
    # print(ind,"done")
    values[conditions[row[1]]][int(row[2]/2)] += row[3]
    count[conditions[row[1]]][int(row[2]/2)] += 1

x_vals = [2*i for i in range(10)]


# for i in range(4):
y_vals = []  # number of participants = 6, each participant will have trial count = 0,2,4,....,18 : 5 times in total. Hence, 6x5=30 for average
for j in range(10):
    y_vals.append(values[0][j]/count[0][j])
plt.plot(x_vals, y_vals)

y_vals = []
for j in range(10):
    y_vals.append(values[1][j]/count[1][j])
plt.plot(x_vals, y_vals)

y_vals = []
for j in range(10):
    y_vals.append(values[2][j]/count[2][j])
plt.plot(x_vals, y_vals)

y_vals = []
for j in range(10):
    y_vals.append(values[3][j]/count[3][j])
plt.plot(x_vals, y_vals)

plt.xlabel("Number of Trials")
plt.ylabel("Total Rewards")
plt.grid()
# plt.tight_layout()
plt.legend(list(conditions.keys()))

plt.show()
