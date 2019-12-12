"""
 The file ex1data2.txt contains a training set of housing prices in Port-
land, Oregon. The first column is the size of the house (in square feet), the
second column is the number of bedrooms, and the third column is the price
of the house
 "perform feature normalizarion "
-Subtract the mean value of each feature from the dataset.
-After subtracting the mean, additionally scale (divide) the feature values
by their respective /standard deviations."
 """
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def reading_data_file(csv_filename):
    df = pd.read_csv(csv_filename, header=None)
    df.columns = [["size", "bedroom", "price"]]
    return df


def normalize(df):
    mean_dataset = np.mean(df, axis=0)  # we should retain mean and std for predictions so passing it via function
    std_dataset = np.std(df, axis=0)
    df = (df - mean_dataset) / std_dataset
    return df, mean_dataset, std_dataset


def fit_data(df):
    x = df[["size", "bedroom"]]
    y = df["price"]
    x = np.c_[np.ones(x.shape[0]), x]  # remember this will always return numpy array
    theta = np.zeros((x.shape[1], 1))  # np.zeros((3, 1))
    alpha = 0.3
    return x, y, theta, alpha


def plot_data(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df["size"], df["bedroom"], df["price"], c="red", marker="o")
    ax.set_xlabel('size of house')
    ax.set_ylabel('No of Bedrooms')
    ax.set_zlabel('price of house')
    plt.title("Housing prices in Port-land, Oregon.")
    plt.savefig("Week3-LinearReg.png")
    plt.show()
    return plt


def h(x, theta):  # this is probability/hypotheses
    return np.dot(x, theta)


def j(x, y, theta):  # this is cost function
    m = x.shape[0]
    hypothesis = h(x, theta)
    error = hypothesis - y
    return 1 / (2 * m) * (np.dot(error.T, error))  # (1/2m)*sum[(error)^2]


def first_der_j(x, y, theta, alpha):  # dj/dQ
    m = x.shape[0]
    hypothesis = h(x, theta)
    error = hypothesis - y
    # return (alpha * (1 / m) * (np.dot(error.T, x))).T
    return alpha * (1 / m) * (np.dot(x.T, error))


def batch_gradient_descent(x, y, theta, alpha):
    m = x.shape[0]
    theta_list = list()  # to append list of all the thetas
    j_list = list()  # to append values of cost
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


def optional_for_troubleshooting(x, y, theta, alpha):
    hypothesis = h(x, theta)
    print("x.shape = ", x.shape)
    print("theta.shape =", theta.shape)
    print("hypothesis.shape =", hypothesis.shape)
    cost = j(x, y, theta)
    print("Initial cost= ", cost)
    print("cost.shape=", cost.shape)
    deri = first_der_j(x, y, theta, alpha)
    print("deri.shape=", deri.shape)


if __name__ == "__main__":
    df = reading_data_file("ex1data2.txt")
    df, mean_dataset, std_dataset = normalize(df)
    x, y, theta, alpha = fit_data(df)
    plot_data(df)
    # optional_for_troubleshooting(x, y, theta,alpha)
    j_list, theta_list, hypothesis, i, deri_theta_list = batch_gradient_descent(x, y, theta, alpha)
    plt = plot_cost_function(j_list, i)
    final_theta = np.ones((3, 1))
    final_theta[0][0] = theta_list[-1][0][0]
    final_theta[1][0] = theta_list[-1][1][0]
    final_theta[2][0] = theta_list[-1][2][0]
    print("final_theta_values =", final_theta)
    print("final_cost_value = ", j_list[-1][0][0])
