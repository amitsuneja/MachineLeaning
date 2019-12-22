import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import scipy.optimize as opt
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt

df = pd.read_csv("ex2data2.txt", header=None)
x = df.iloc[:, :-1].values  # return dataframe , all field except last field
y = df.iloc[:, -1].values   # return series , last field
y = y[:, np.newaxis]  # turn shape of y from Series of shape(118,) to Numpy array (118,1)

poly = PolynomialFeatures(6)
x = poly.fit_transform(x)  # convert (118,2) into polynomial of (118,28)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))  # note outer brackets in denominator are important else it bad/wrong result.


def cost_function(theta, x,  y, Lambda):
    m = x.shape[0]
    h = sigmoid(x @ theta)  # h = (118, 28)@(28, 1) = (118, 1)
    # error = (-y * np.log(h)) - ((1-y)*np.log(1-h))
    # j = 1/m * sum(error)
    j = (1/m) * (np.dot(np.log(h).T, -y) - np.dot(np.log(1 - h).T, (1 - y)))

    # Regularization Term
    # reg_term = (Lambda/2*m)*(np.dot(theta.T, theta))
    reg_term = Lambda/(2*m) * sum(theta**2)
    j = j + reg_term
    return j


def first_deri_j(theta, x,  y, Lambda):
    m = x.shape[0]
    h = sigmoid(x @ theta)  # h = (118, 28)@(28, 1) = (118, 1)
    derivative = 1/m * np.dot(x.T, (h-y))  # (h - y)x = (118, 1)-(118, 1) = (118, 28).T @ (118, 1) = (28, 1)
    derivative[1:] = derivative[1:] + (Lambda/m) * theta[1:]  # (28, 1)
    # j_0 = 1/m * (x.T @ (h - y))[0]
    # j_1 = 1/m * (x.T @ (h - y))[1:] + (Lambda/m) * theta[1:]
    # derivative = np.vstack((j_0[:, np.newaxis], j_1))
    return derivative    # this can be also written as j[0,0]


def gradient_descent(theta, x,  y, Lambda, alpha, iterations):
    m = len(y)
    cost_list = list()
    for i in range(iterations):
        cost = cost_function(theta, x,  y, Lambda)
        derivation = first_deri_j(theta, x,  y, Lambda)
        theta = theta - (alpha*derivation)
        cost_list.append(cost)
    return theta, cost_list


m, n = x.shape  # m, n means row, columns of matrix , so m means rows and n means columns.
theta_initial = np.zeros(n).reshape(n, 1)  # alternate theta_initial = np.zeros((n,1))
Lambda = 1
initial_cost = cost_function(theta_initial, x,  y, Lambda)
print("initial_cost=", initial_cost)
final_theta, cost_list = gradient_descent(theta_initial, x,  y, 1, 0.3, 500)
final_cost, = cost_function(final_theta, x,  y, Lambda)
print("final_cost=", final_cost)


# Accuracy of model
p = np.dot(x, final_theta) > 0
accuracy = (np.mean(p == y)) * 100
print("accuracy = {:.2f}%".format(accuracy))
print("______________________________________________________________________________")
theta_initial = np.zeros(n).reshape(n, 1)  # alternate theta_initial = np.zeros((n,1))
output = opt.fmin_tnc(func=cost_function, x0=theta_initial.flatten(),
                      fprime=first_deri_j, args=(x, y.flatten(), Lambda))
theta = output[0]
final_cost, = cost_function(final_theta, x,  y, Lambda)
print("final_cost=", final_cost)
# Accuracy of model
p = np.dot(x, final_theta) > 0
print(p.shape)
print(y.shape)
accuracy = (np.mean(p == y)) * 100
print("accuracy = {:.2f}%".format(accuracy))


















# df = pd.read_csv('ex2data2.txt', header=None)
# df.columns = ['x1', 'x2', 'y']
# mask = df["y"] == 1
# x1_pass = df[mask]["x1"]
# x2_pass = df[mask]["x2"]
# x1_fail = df[~mask]["x1"]
# x2_fail = df[~mask]["x2"]
# plt.scatter(x1_pass, x2_pass, marker="o", color="green", label="pass")
# plt.scatter(x1_fail, x2_fail, marker="o", color="red", label="fail")
# plt.legend()
# plt.xlabel("test1")
# plt.ylabel("test2")
# plt.show()





























