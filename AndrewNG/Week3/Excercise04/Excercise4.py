import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import scipy.optimize as opt    # more on this later

"""
https://towardsdatascience.com/andrew-ngs-machine-learning-course-in-python-regularized-logistic-regression-lasso-regression-721f311130fb
https://www.kaggle.com/ashishrane7/logistic-regression-non-linear-decision-boundary/notebook
https://anaconda.org/rafaelhbarros/logistic_regression/notebook
https://medium.com/analytics-vidhya/python-implementation-of-andrew-ngs-machine-learning-course-part-2-2-dceff1a12a12
"""

"""
You will implement regularized logistic regression to predict whether microchips from a fabrication 
plant passes quality assurance (QA). During QA, each microchip goes through various tests to ensure it is 
functioning correctly.
Suppose you are the product manager of the factory and you have the test results for some microchips on two 
different tests. From these two tests, you would like to determine whether the microchips should be accepted 
or rejected. To help you make the decision, you have a dataset of test results on past microchips, 
from which you can build a logistic regression model.
"""


def z(x, theta):
    return np.dot(x, theta)


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))  # note outer brackets in denominator are important else it bad/wrong result.


def cost_function(theta, x, y, reg_factor_Lambda):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    j = (1 / m) * (np.dot(np.log(h).T, -y) - np.dot(np.log(1 - h).T, (1 - y)))

    # Regularization Term
    # reg_term = (reg_factor_Lambda * np.dot(theta.T, theta)) / (2 * m)
    reg_term = (reg_factor_Lambda * sum(theta**2))/(2 * m)
    # Regularized cost
    j = j + reg_term
    return j


def first_deri_j(theta, x, y, reg_factor_Lambda):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    calculation = np.zeros([m, 1])
    calculation = (1 / m) * np.dot(x.T, (h - y))
    calculation[1:] = calculation[1:] + (reg_factor_Lambda / m) * theta[1:]
    return calculation


df = pd.read_csv('ex2data2.txt', header=None)
df.columns = ['x1', 'x2', 'y']
mask = df["y"] == 1
x1_pass = df[mask]["x1"]
x2_pass = df[mask]["x2"]
x1_fail = df[~mask]["x1"]
x2_fail = df[~mask]["x2"]
plt.scatter(x1_pass, x2_pass, marker="o", color="green", label="pass")
plt.scatter(x1_fail, x2_fail, marker="o", color="red", label="fail")
plt.legend()
plt.xlabel("test1")
plt.ylabel("test2")
plt.show()
plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window


x = df[df.columns[:-1]].values
poly = PolynomialFeatures(6)
x = (poly.fit_transform(x))
"""this has converted (118,2) into (118, 28) . So from 2 col/dimension  to 28 col/dimension"""
y = df.iloc[:, 2]
# print(x.shape)
# Set the regularization factor to 1
reg_factor_Lambda = 1
(m, n) = x.shape
y = y[:, np.newaxis]
theta = np.zeros((n, 1))
reg_factor_Lambda = 1
Initial_Cost = cost_function(theta, x, y, reg_factor_Lambda)
print("Initial_Cost =", Initial_Cost)
output = opt.fmin_tnc(func=cost_function, x0=theta.flatten(),
                      fprime=first_deri_j, args=(x, y.flatten(), reg_factor_Lambda))
theta = output[0]
print(theta)  # theta contains the optimized values


# Accuracy of model
prediction = sigmoid(z(x, theta)) >= 0.5
accuracy = np.mean(prediction == y.flatten()) * 100
print("accuracy = {:.2f}%".format(accuracy))
print("theta.shape= ", theta.shape)

# Decision Boundary
u = np.linspace(-1, 1.5, 50)
v = np.linspace(-1, 1.5, 50)
z = np.zeros((len(u), len(v)))
poly = PolynomialFeatures(6)
for i in range(len(u)):
    for j in range(len(v)):
        my_array = np.array([[u[i]], [v[j]]]).reshape(1, 2)
        z[i, j] = np.dot(poly.fit_transform(my_array), theta)
plt.scatter(x1_pass, x2_pass, marker="o", color="green", label="pass")
plt.scatter(x1_fail, x2_fail, marker="o", color="red", label="fail")
plt.contour(u, v, z, 0)
plt.legend()
plt.xlabel("test1")
plt.ylabel("test2")
plt.show()

