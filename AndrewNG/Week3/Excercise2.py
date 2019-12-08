"""
https://medium.com/analytics-vidhya/python-implementation-of-andrew-ngs-machine-learning-course-part-2-2-dceff1a12a12
Make sure to read maths formula given in this page as it is typical cost function.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt  # more on this later

data = pd.read_csv('ex2data2.txt', header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, 2]
print(X)
print(y)
"""
Lets visualize the data
"""
mask = y == 1
passed = plt.scatter(X[mask][0].values, X[mask][1].values)
failed = plt.scatter(X[~mask][0].values, X[~mask][1].values)
plt.xlabel('Microchip Test1')
plt.ylabel('Microchip Test2')
plt.legend((passed, failed), ('Passed', 'Failed'))
plt.show()

"""
Feature Mapping:
We have two independent features and one dependent variable.
Here 0 means the chip has been rejected and 1 means accepted.

One way to fit the data better is to create more features from each data point. Hence we will map the features
into all polynomial terms of x1 and x2 up to the sixth power.

As a result of this mapping, our vector of two features (the scores on two QA tests) has been transformed into a
28-dimensional vector. A logistic regression classifier trained on this higher-dimension feature vector
will have a more complex decision boundary and will appear nonlinear when drawn in our 2-dimensional plot.

While the feature mapping allows us to build a more expressive classifier, it is also more susceptible to over
fitting. In the next parts of the exercise, you will implement regularized logistic regression to fit the data
and also see for yourself how regularization can help combat the over fitting problem.
"""


def mapFeature(X1, X2):
    degree = 6
    out = np.ones(X.shape[0])[:, np.newaxis]
    print("out=", out)
    print("out shape=", out.shape)
    for i in range(1, degree + 1):
        for j in range(i + 1):
            out = np.hstack((out, np.multiply(np.power(X1, i - j), np.power(X2, j))[:, np.newaxis]))
    return out


X = mapFeature(X.iloc[:, 0], X.iloc[:, 1])
# print(X.shape)  # (118, 28) where 118 is number of data numbers present and 28 is dimension of data.


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def lrCostFunction(theta_t, X_t, y_t, lambda_t):
    m = len(y_t)
    J = (-1 / m) * (y_t.T @ np.log(sigmoid(X_t @ theta_t)) + (1 - y_t.T) @ np.log(1 - sigmoid(X_t @ theta_t)))
    reg = (lambda_t / (2 * m)) * (theta_t[1:].T @ theta_t[1:])
    J = J + reg
    return J


def lrGradientDescent(theta, X, y, lambda_t):
    m = len(y)
    grad = np.zeros([m, 1])
    grad = (1 / m) * X.T @ (sigmoid(X @ theta) - y)
    grad[1:] = grad[1:] + (lambda_t / m) * theta[1:]
    return grad


(m, n) = X.shape
y = y[:, np.newaxis]
theta = np.zeros((n, 1))
lmbda = 1
J = lrCostFunction(theta, X, y, lmbda)
print(J)

"""
fmin_tnc is an optimization solver that finds the minimum of an unconstrained function. For logistic regression,
you want to optimize the cost function with the parameters theta.

"""

output = opt.fmin_tnc(func=lrCostFunction, x0=theta.flatten(), fprime=lrGradientDescent, args=(X, y.flatten(), lmbda))
theta = output[0]
# print(theta)  # theta contains the optimized values

"""
Note on flatten() function: Unfortunately scipy’s fmin_tnc doesn’t work well with column or row vector.
It expects the parameters to be in an array format. The flatten() function reduces a column or row vector
into array format.
"""

"""
Accuracy of model
Lets try to find the model accuracy by predicting the outcomes from our learned parameters and then
comparing with the original outcomes.
"""
pred = [sigmoid(np.dot(X, theta)) >= 0.5]
print("model accuracy = ", np.mean(pred == y.flatten()) * 100)

"""
Plotting Decision Boundary (optional)
To help you visualize the model learned by this classifier, we will plot the (non-linear) decision boundary
that separates the positive and negative examples. We plot the non-linear decision boundary by computing the
classifier’s predictions on an evenly spaced grid and then drew a contour plot of where the predictions change
from y = 0 to y = 1.
"""
u = np.linspace(-1, 1.5, 50)
v = np.linspace(-1, 1.5, 50)
z = np.zeros((len(u), len(v)))


def mapFeatureForPlotting(X1, X2):
    degree = 6
    out = np.ones(1)
    for i in range(1, degree + 1):
        for j in range(i + 1):
            out = np.hstack((out, np.multiply(np.power(X1, i - j), np.power(X2, j))))
    return out


for i in range(len(u)):
    for j in range(len(v)):
        z[i, j] = np.dot(mapFeatureForPlotting(u[i], v[j]), theta)
mask = y.flatten() == 1
X = data.iloc[:, :-1]
passed = plt.scatter(X[mask][0], X[mask][1])
failed = plt.scatter(X[~mask][0], X[~mask][1])
plt.contour(u, v, z, 0)
plt.xlabel('Microchip Test1')
plt.ylabel('Microchip Test2')
plt.legend((passed, failed), ('Passed', 'Failed'))
plt.show()
