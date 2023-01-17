#Experiment 2
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

data = pd.read_csv('Salary_Data.csv')
x = data['YearsExperience'].to_numpy().reshape(-1,1)
y = data['Salary'].to_numpy().reshape(-1,1)

X = #fill code
theta =#fill code using eq.3
print(theta)y_pre = X.dot(theta)

print("Mean squared error2: %.7f" % mean_squared_error( y, y_pre))

plt.scatter(x, y)
plt.plot(x, y_pre, color='blue')
plt.show()