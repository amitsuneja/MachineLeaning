import numpy as np
import matplotlib.pyplot as plt


def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau))


def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1, x0]
    X = np.c_[np.ones(len(X)), X]
    # fit model: normal equations with kernel
    xw = X.T * radial_kernel(x0, X, tau)
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    # predict value
    return x0 @ beta


def generate_data():
    n = 1000
    X = np.linspace(-3, 3, num=n)
    Y = np.log(np.abs(X ** 2 - 1) + .5)
    # Y = np.sin(X) + 0.3 * np.random.randn(n)  #
    plt.scatter(X, Y, s=5, color="green")
    plt.savefig("LocalWeightedLinearRegression2-DataInitial.png")
    plt.cla()  # Clear axis
    plt.clf()  # Clear figure
    plt.close()  # Close a figure window
    # jitter X
    X += np.random.normal(scale=.1, size=n)
    plt.scatter(X, Y, s=5, color="green")
    plt.savefig("LocalWeightedLinearRegression2-DatawithGitter.png")
    plt.cla()  # Clear axis
    plt.clf()  # Clear figure
    plt.close()  # Close a figure window
    return X, Y


def create_plot(X, Y, tau):
    fig, axes = plt.subplots(3, 2, figsize=(16, 8), sharex=False, sharey=False, dpi=120)
    # plt.subplots(3, 2 ) means display data in 3 rows and 2 columns
    # Plot each axes
    for i, ax in enumerate(axes.ravel()):
        domain = np.linspace(-3, 3, num=40)
        prediction = [local_regression(x0, X, Y, tau[i]) for x0 in domain]
        ax.scatter(X, Y, s=5, color="green", label="actual")
        ax.scatter(domain, prediction, s=5, color='red', label="prediction")
        ax.set(
            title="tau=" + str(tau[i]),
            xlabel='X',
            ylabel='Y',
         )
        ax.legend(loc='best')
    plt.suptitle('Local Weight Linear regression', size=10, color='blue')
    plt.savefig("LocalWeightedLinearRegression2-DataAndPrediction.png")
    return plt


if __name__ == "__main__":
    X, Y = generate_data()
    tau = [800, 10, .1, .01, .08, .9]
    myplot = create_plot(X, Y, tau)
    myplot.show()

