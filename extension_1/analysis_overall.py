import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

untimed_values = [0 for j in range(4)]
timed_values = [0 for j in range(4)]
untimed_count = [0 for j in range(4)]
timed_count = [0 for j in range(4)]

for ind, row in enumerate(data_untimed):
    untimed_values[conditions[row[1]]] += row[2]
    untimed_count[conditions[row[1]]] += 1

x_vals = [2*i for i in range(11)]


for ind, row in enumerate(data_timed):
    timed_values[conditions[row[1]]] += row[2]
    timed_count[conditions[row[1]]] += 1


# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
condition = list(conditions.keys())
avg_rewards_untimed = [x/y for (x, y) in zip(untimed_values, untimed_count)]
avg_rewards_timed = [x/y for (x, y) in zip(timed_values, timed_count)]
  



X = list(condition)
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, avg_rewards_untimed, 0.4, label = 'untimed')
plt.bar(X_axis + 0.2, avg_rewards_timed, 0.4, label = 'timed')
  
plt.xticks(X_axis, X)
plt.xlabel("Payoff Condition")
plt.ylabel("Average Penalty Incurred")
plt.title("Average Penalty across each payoff condition")
plt.legend()
plt.show()
