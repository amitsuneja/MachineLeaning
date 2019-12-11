import csv
import numpy as np
import matplotlib.pyplot as plt

filename = "sample1.csv"
def loadCSV(filename):
    '''
    function to load dataset
    '''
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
    print(dataset)
    return np.array(dataset)



def normalize(X):
    '''
    function to normalize feature matrix, X
    '''
    mins = np.min(X, axis=0)
    maxs = np.max(X, axis=0)
    rng = maxs - mins
    norm_X = 1 - ((maxs - X) / rng)
    return norm_X


def logistic_func(theta, X):
    '''
    logistic(sigmoid) function
    '''
    return 1.0 / (1 + np.exp(-np.dot(X, theta.T)))


def log_gradient(theta, X, y):
    '''
    logistic gradient function
    '''
    first_calc = logistic_func(theta, X) - y.reshape(X.shape[0], -1)
    final_calc = np.dot(first_calc.T, X)
    return final_calc


def cost_func(theta, X, y):
    '''
    cost function, J
    '''
    log_func_v = logistic_func(theta, X)
    y = np.squeeze(y)
    step1 = y * np.log(log_func_v)
    step2 = (1 - y) * np.log(1 - log_func_v)
    final = -step1 - step2
    return np.mean(final)


def grad_desc(X, y, theta, lr=.01, converge_change=.001):
    '''
    gradient descent function
    '''
    cost = cost_func(theta, X, y)
    change_cost = 1
    num_iter = 1

    while (change_cost > converge_change):
        old_cost = cost
        theta = theta - (lr * log_gradient(theta, X, y))
        cost = cost_func(theta, X, y)
        change_cost = old_cost - cost
        num_iter += 1
    return theta, num_iter

def plot_reg(X, y, theta):
    '''
    function to plot decision boundary
    '''
    # labelled observations
    x_0 = X[np.where(y == 0.0)]
    x_1 = X[np.where(y == 1.0)]

    # plotting points with diff color for diff label
    plt.scatter([x_0[:, 1]], [x_0[:, 2]], c='b', label='y = 0')
    plt.scatter([x_1[:, 1]], [x_1[:, 2]], c='r', label='y = 1')

    # plotting decision boundary
    x1 = np.arange(0, 1, 0.1)
    x2 = -(theta[0, 0] + theta[0, 1] * x1) / theta[0, 2]
    plt.plot(x1, x2, c='k', label='reg line')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # load the dataset
    dataset = loadCSV(filename)

    # normalizing feature matrix
    X = normalize(dataset[:, :-1])

    # stacking columns wth all ones in feature matrix
    X = np.hstack((np.matrix(np.ones(X.shape[0])).T, X))

    # response vector
    y = dataset[:, -1]

    # initial theta values
    theta = np.matrix(np.zeros(X.shape[1]))

    # theta values after running gradient descent
    theta, num_iter = grad_desc(X, y, theta)

    # estimated theta values and number of iterations
    print("Estimated regression coefficients:", theta)
    print("No. of iterations:", num_iter)

    # plotting regression line
    plot_reg(X, y, theta)