import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("overall_data.csv", delimiter=",", header=0)
data = data.iloc[:,:].values


conditions = {
    " IOWA": 0,
    " Equal Means": 1,
    " Low Var": 2,
    " High Var": 3
}

values = [0 for j in range(4)]
rep_values = [0 for j in range(4)]
count = [0 for j in range(4)]
rep_count = [0 for j in range(4)]

for ind, row in enumerate(data):
    values[conditions[row[1]]] += row[2]
    count[conditions[row[1]]] += 1
    rep_values[conditions[row[1]]] += row[3]
    rep_count[conditions[row[1]]] += 1

condition = list(conditions.keys())
avg_rewards = [x/y for (x, y) in zip(values, count)] 
rep_choices =  [x/y for (x, y) in zip(rep_values, rep_count)]

X = list(condition)
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis, avg_rewards, 0.4, label = 'untimed')  
plt.xticks(X_axis, X)
plt.xlabel("Payoff Condition")
plt.ylabel("Average Reward Gained")
plt.title("Average Reward across each payoff condition")
plt.show()

plt.bar(X_axis, rep_choices, 0.4, label = 'untimed')  
plt.xticks(X_axis, X)
plt.xlabel("Payoff Condition")
plt.ylabel("Repeat Choices made")
plt.title("Average Repeat Choices across each payoff condition")
plt.show()
