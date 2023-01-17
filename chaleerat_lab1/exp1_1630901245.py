#Experiment 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statistics import mean

data = pd.read_csv('Salary_Data.csv')
x = data['YearsExperience'].to_numpy().reshape(-1,1)
y = data['Salary'].to_numpy().reshape(-1,1)
meanx = np.mean(x)
meany = np.mean(y)
plt.scatter(x,y)
plt.show()

n = x.size
upper_eq = sum(x*y)-(sum(x)*sum(y)/n)
lower_eq = sum(x**2)-n*(meanx**2)
m = upper_eq/lower_eq
b = meany-m*(meanx)
y_pre = m * x + b
print(f'm = {m}')
print(f'b = {b}')
print("Mean squared error1: %.7f" % mean_squared_error( y, y_pre))

plt.plot(x,y_pre,color = 'red')
plt.scatter(x,y)
plt.show()

def user():
    x = float(input("Enter YearsExperience:"))
    salary = m * x + b
    return print(f"Salary is{salary}")
user()