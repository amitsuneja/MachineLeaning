"""
Linear regression with one variable

DataFile - ex1data1.txt
m(number of records) = 96 and n(number of features) = 1

The first column is the population of a city and the second column is
the profit of a food truck in that city.

A negative value for profit indicates a loss.



"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def reading_data_file(csv_filename):
    df = pd.read_csv(csv_filename, header=None)
    df.columns = ["population", "profit"]
    return df


def plot_data(df):
    plt.scatter(df["population"], df["profit"], c="red", marker="o", label="profit v/s popultion")
    plt.xlabel("Population of City in 10,000s")
    plt.ylabel("Profit in $10,000s")
    plt.title("My Company Data")
    plt.legend()
    plt.savefig("Week2-LinearRegOneVariable.png")
    return plt


def fit_data(df):
    x = df["population"]
    y = df["profit"]
    y = y[np.newaxis, :]
    x = np.c_[np.ones(x.shape[0]), x]  # remember this will always return numpy array
    theta = np.zeros((x.shape[1], 1))  #np.zeros((2, 1))
    alpha = 0.01
    return x, y, theta, alpha


def h(x, theta):                      # this is probability/hypotheses
    return np.dot(x, theta)


def j(x, y, theta):                    # this is cost function
    m = x.shape[0]
    hypothesis = h(x, theta)
    print(hypothesis.shape)
    print(y.shape)
    error = hypothesis - y.T
    return 1 / (2 * m) * (np.dot(error.T, error))    # (1/2m)*sum[(error)^2]


def first_der_j(x, y, theta, alpha):  # dj/dQ
    m = x.shape[0]
    hypothesis = h(x, theta)
    error = hypothesis - y
    # return (alpha * (1 / m) * (np.dot(error.T, x))).T
    """
    above statement and below statement are doing same job ,why ? check basic of matrix. 
    x = np.arange(194).reshape(97, 2)
    error = np.arange(97).reshape(97, 1)
    print("x.shape=", x.shape)                                     # x= (97, 2)
    print("error.shape=", error.shape)                             # error= (97, 1)
    print("np.dot(x.T, error).shape =", np.dot(x.T, error).shape)  # ---> (2,1)
    print("np.dot(error.T, x).T.shape =",  np.dot(error.T, x).T.shape)  # ---> (2,1)
    """
    return alpha * (1 / m) * (np.dot(x.T, error))


def batch_gradient_descent(x, y, theta, alpha):
    m = x.shape[0]
    theta_list = list()  # to append list of all the thetas
    j_list = list()      # to append values of cost
    j_list.append(1e10)  # we append some large value to the cost list
    deri_theta_list = list()
    i = 0
    run = True
    while run:
        theta = theta - first_der_j(x, y, theta, alpha)
        cost = j(x, y, theta)
        j_list.append(cost)
        theta_list.append(theta)
        deri_theta_list.append(first_der_j(x, y, theta, alpha))

        if j_list[i] - j_list[i + 1] < 1e-9:  # checking if the change in cost function is less than 10^(-9)
            run = False
        # print("Iteration number {} have cost = {}".format(i, cost))
        i = i + 1
    j_list.pop(0)
    hypothesis = h(x, theta)
    return j_list, theta_list, hypothesis, i, deri_theta_list


def plot_cost_function(j_list, i):
    x = [k[0][0] for k in j_list]
    y = range(i)
    plt.plot(y, x)
    plt.ylabel("Cost")
    plt.xlabel("No of iterations")
    plt.savefig("Week2-costfunction.png")
    plt.cla()  # Clear axis
    plt.clf()  # Clear figure
    plt.close()  # Close a figure window
    return plt


def plot_regression_line(df, x, final_theta):
    plt = plot_data(df)
    plt.plot(x[:, 1], h(x, final_theta))
    plt.savefig("Week2-LinearRegOneVariable-final.png")


def optional_for_troubleshooting(x, y, theta,alpha):
    hypothesis = h(x, theta)
    print("x.shape = ", x.shape)
    print("theta.shape =", theta.shape)
    print("hypothesis.shape =",  hypothesis.shape)
    cost = j(x, y, theta)
    print("Initial cost= ", cost)
    print("cost.shape=", cost.shape)
    deri = first_der_j(x, y, theta, alpha)
    print("deri =", deri )
    print("deri.shape=", deri.shape)


if __name__ == "__main__":
    df = reading_data_file("ex1data1.txt")
    plt = plot_data(df)
    x, y, theta, alpha = fit_data(df)
    optional_for_troubleshooting(x, y, theta,alpha)
    # j_list, theta_list, hypothesis, i, deri_theta_list = batch_gradient_descent(x, y, theta, alpha)
    # plt = plot_cost_function(j_list, i)
    # final_theta = np.ones((2, 1))
    # final_theta[0][0] = theta_list[-1][0][0]
    # final_theta[1][0] = theta_list[-1][1][0]
    # print("final_theta_values =", final_theta)
    # print("final_cost_value = ", j_list[-1][0][0])
    # plt = plot_regression_line(df , x  , final_theta)






















