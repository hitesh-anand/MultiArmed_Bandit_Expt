import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

data_untimed = pd.read_csv("untimed_overall_data.csv", delimiter=",", header=0)
data_untimed = data_untimed.iloc[:,:].values

data_timed = pd.read_csv("timed_overall_data.csv", delimiter=",", header=0)
data_timed = data_timed.iloc[:,:].values

conditions = {
    " IOWA": 0,
    " Equal Means": 1,
    " Low Var": 2,
    " High Var": 3
}

untimed_total = 0
timed_total = 0
# untimed_ = 0
# timed_total = 0

untimed_points = []
timed_points = []

for row in data_untimed:
    untimed_total += row[3]
    untimed_points.append(row[3])

for row in data_timed:
    timed_total += row[3]
    timed_points.append(row[3])

new_points = []

for i in range(0, len(untimed_points), 4):
    new_points.append(sum(untimed_points[i:i+4]))
    new_points.append(sum(timed_points[i:i+4]))

print(len(new_points))

deltas = [random.randint(0,30)/30 for i in range(len(new_points)//2)]

print(deltas)

timed_x = [10-deltas[i] for i in range(len(new_points)//2)]
untimed_x = [15-deltas[i] for i in range(len(new_points)//2)]
# x_vals = [2*i for i in range(11)]

timed_y = [new_points[i] for i in range(1, len(new_points), 2)]
untimed_y = [new_points[i] for i in range(0, len(new_points), 2)]

plt.scatter(timed_x, timed_y, c='blue', label="timed")
plt.scatter(untimed_x, untimed_y, c='red', label="untimed")
plt.scatter([15], [untimed_total/15], marker='x', sizes=[50])
plt.scatter([10], [timed_total/15], marker='o', sizes=[50])
plt.xticks([10, 15], ["timed", "untimed"])
plt.legend()

for i in range(15):
    x_vals = [timed_x[i], untimed_x[i]]
    y_vals = [timed_y[i], untimed_y[i]]
    plt.plot(x_vals, y_vals, alpha=0.2)
plt.title("Repeat choices made under untimed/timed conditions")
plt.show()



# plt.show()
