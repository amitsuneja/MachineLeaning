import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_data_file():
    x = pd.read_csv("ex4Data/ex4x.dat", header=None)
    y = pd.read_csv("ex4Data/ex4y.dat", header=None)
    df = pd.concat([x, y], axis=1, sort=False)
    df.columns = ["EXAM1", "EXAM2", "PASSORFAIL"]
    return df


def plot_initial_data(df):
    mask_1_pass = df["PASSORFAIL"] == 1
    mask_0_fail = df["PASSORFAIL"] == 0
    plt.scatter(df[mask_1_pass]["EXAM1"], df[mask_1_pass]["EXAM2"], c="green", marker="+", label="Admitted")
    plt.scatter(df[mask_0_fail]["EXAM1"], df[mask_0_fail]["EXAM2"], c="red", marker="o", label="Not Admitted")
    plt.xlabel("EXAM1 Score")
    plt.ylabel("EXAM2 Score")
    plt.legend()
    return plt


def fit(df):
    x = df[["EXAM1", "EXAM2"]]
    y = df[["PASSORFAIL"]]
    x = np.c_[np.ones(df.shape[0]), df[["EXAM1", "EXAM2"]]]  # this line convert x into array
    theta = np.ones((1, x.shape[1]))
    return x, y, theta


def z(x, theta):
    return np.dot(x, theta.T)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def j(x, y, theta):
    h = sigmoid(z(x, theta))
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

if __name__ == "__main__":
    df = read_data_file()
    # plt = plot_initial_data(df)
    x, y, theta = fit(df)
    print("x.shape=", x.shape)
    print("theta.T shape =", theta.T.shape)
    z = z(x, theta)
    print("z = (X,theta.T) =", z.shape)
    h = sigmoid(z)
    print("hypothesis h.shape =", h.shape)
    print("y.shape =", y.shape)
    cost = j(x, y, theta)








