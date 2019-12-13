import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
https://medium.com/@martinpella/logistic-regression-from-scratch-in-python-124c5636b8ac
https://www.geeksforgeeks.org/understanding-logistic-regression/
"""

def normalize(X):
    mins = np.min(X, axis=0)
    maxs = np.max(X, axis=0)
    rng = maxs - mins
    norm_X = 1 - ((maxs - X) / rng)
    return norm_X


def calc_z(X, theta):
    return np.dot(X, theta)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def cost_function(X, y, theta):
    z = calc_z(X, theta)
    h = sigmoid(z)
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


def derivative_of_cost_function(X, y, theta):
    z = calc_z(X, theta)
    h = sigmoid(z)
    calculation = np.dot((h - y).T, X)
    return calculation.T


def grad_desc(X, y, theta, lr=.01, converge_change=0.001):
    cost_list = []
    cost = cost_function(X, y, theta)
    cost_list.append(cost)
    i = 0
    run = True
    while run:
        theta = theta - lr * derivative_of_cost_function(X, y, theta)
        cost = cost_function(X, y, theta)
        cost_list.append(cost)
        print("Value of i = {} and i+1 ={}".format(i, i+1))
        print("cost[{}] = {} and cost[{}] = {}".format(i, cost_list[i], i+1, cost_list[i+1]))
        print("cost_list[{}] - cost_list[{}] = {} ".format(i, i+1, cost_list[i] - cost_list[i + 1] ))
        if cost_list[i] - cost_list[i + 1] < converge_change:
            run = False
        i += 1
    return theta, i, cost_list



def draw_cost_function(cost_list):
    plt.title('Cost Function J', size=30)
    plt.xlabel('No. of iterations', size=20)
    plt.ylabel('Cost', size=20)
    plt.plot(cost_list)
    plt.savefig("LogisticRegressionFirstBinaryClassifier-CostFunction.png")
    plt.cla()  # Clear axis
    plt.clf()  # Clear figure
    plt.close()  # Close a figure window


def plot_reg(X, y, theta):
    # labelled observations
    x_0 = df[(df["AdmissionStatus"] == 0)]
    x_1 = df[(df["AdmissionStatus"] == 1)]
    # plotting points with diff color for diff label
    plt.scatter(x_0['Maths'], x_0['Physics'], c='b', label='y = 0')
    plt.scatter(x_1['Maths'], x_1['Physics'], c='r', label='y = 1')
    # plotting decision boundary
    x1 = np.arange(0, 1, .01)
    x2 = -(theta[0] + theta[1] * x1) / theta[2]
    plt.plot(x1, x2, c='k', label='reg line')
    plt.xlabel('Maths')
    plt.ylabel('Physics')
    plt.legend()
    plt.savefig("LogisticRegressionFirstBinaryClassifier-DecisionBoundry.png")
    return plt


filename = "../../Excercise03/ex2data1.txt"
#filename = "sample1.csv"
df = pd.read_csv(filename, header=None)
df = normalize(df)
df.columns = ["Maths", "Physics", "AdmissionStatus"]
X = np.array(df[["Maths", "Physics"]])
y = np.array(df[["AdmissionStatus"]])
X = np.c_[np.ones(X.shape[0]), X]
theta = np.ones((X.shape[1], 1))
temp = cost_function(X, y, theta)
print(temp)
theta, num_of_iter, cost_list = grad_desc(X, y, theta)
draw_cost_function(cost_list)
print("final theta_0 =", theta[0])
print("final theta_1 =", theta[1])
print("final theta_2 =", theta[2])
print("Total Number of iterations = ", num_of_iter)
plt = plot_reg(X, y, theta)
plt.show()
print("final_cost =", cost_function(X, y, theta))








