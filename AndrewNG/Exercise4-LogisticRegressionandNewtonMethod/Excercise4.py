
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def normalize(X):
    mins = np.min(X, axis=0)
    maxs = np.max(X, axis=0)
    rng = maxs - mins
    norm_X = 1 - ((maxs - X) / rng)
    return norm_X


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def z(x, theta):
    return np.dot(x, theta)


def j(x, y, theta):
    h = sigmoid(z(x, theta))
    return (-y * np.log(h) - (1 - y) * np.log(1 - h))/80

def gradient(x, y, theta):
    h = sigmoid(z(x, theta))
    return (np.dot((h - y).T, x))/80


def hessian(x, theta):
    h = sigmoid(z(x, theta))
    H = np.dot(np.dot(np.dot((h), (1-h).T), x),x.T)
    H = H/80
    return np.linalg.pinv(H)


def calculation(x, y, theta):
    hessian_inv = hessian(x, theta)
    grad = gradient(x, y, theta)
    cost = j(x, y, theta)

    return np.dot(np.dot(hessian_inv, grad) * cost)


def newton_rapstion(x, y, theta, converge_change=0.001):
    cost_list = []
    cost = j(x, y, theta)
    cost_list.append(cost)
    i = 0
    run = True
    while run:
        theta = theta - calculation(x, y, theta)
        cost = j(x, y, theta)
        cost_list.append(cost)
        # print("Value of i = {} and i+1 ={}".format(i, i+1))
        # print("cost[{}] = {} and cost[{}] = {}".format(i, cost_list[i], i+1, cost_list[i+1]))
        # print("cost_list[{}] - cost_list[{}] = {} ".format(i, i+1, cost_list[i] - cost_list[i + 1] ))
        if cost_list[i] - cost_list[i + 1] < converge_change:
            run = False
        i += 1
    return theta, i, cost_list

# ###################################################################
# filename = "sample1.csv"
# df = pd.read_csv(filename, header=None)
# df = normalize(df)
# df.columns = ["EXAM1", "EXAM2", "PASSORFAIL" ]
# X = np.array(df[["EXAM1", "EXAM2"]])
# y = np.array(df[["PASSORFAIL"]])
# ####################################################################
x = pd.read_csv("ex4Data/ex4x.dat", header=None)
x = normalize(x)
y = pd.read_csv("ex4Data/ex4y.dat", header=None)
df = pd.concat([x, y], axis=1, sort=False)
df.columns = ["EXAM1", "EXAM2", "PASSORFAIL" ]
####################################################################
mask_1_pass = df["PASSORFAIL"] == 1
mask_0_fail = df["PASSORFAIL"] == 0
plt.scatter(df[mask_1_pass]["EXAM1"], df[mask_1_pass]["EXAM2"], c="green", marker="+", label="Admitted")
plt.scatter(df[mask_0_fail]["EXAM1"], df[mask_0_fail]["EXAM2"], c="red", marker="o", label="Not Admitted")
plt.xlabel("EXAM1 Score")
plt.ylabel("EXAM2 Score")
plt.legend()
#plt.show()
x = df[["EXAM1", "EXAM2"]]
y = df[["PASSORFAIL"]]
x = np.c_[np.ones(df.shape[0]), df[["EXAM1", "EXAM2"]]]
theta = np.ones((x.shape[1], 1))
Amit = calculation(x, y,  theta)
print(Amit)


