import numpy as np  # Numeriacal computing
import matplotlib.pyplot as plt  # plotting core
import seaborn as sns  # higher level plotting tools


def g(z):
    return 1/(1 + np.exp(-z))


def test_g():
    x = np.linspace(-10, 10, 100)
    plt.plot(x, g(x))
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("Sigmoid(X)")
    plt.annotate('Convex', (-7.5, 0.2), fontsize=18)
    plt.annotate('Concave', (3, 0.8), fontsize=18)
    plt.title("Sigmoid Function g(z) = 1/(1 + exp(-z))", fontsize=12, color="blue")
    plt.show()
    plt.cla()  # Clear axis
    plt.clf()  # Clear figure
    plt.close()  # Close a figure window


def plot_cost_function():
    x = np.linspace(-10, 10, 100)
    plt.plot(g(x), -np.log(g(x)))
    plt.plot(g(x), -np.log(1-g(x)))
    plt.xlabel("g(x)", fontsize=12, color="blue")
    plt.ylabel("cost", fontsize=12, color="blue")
    plt.annotate('- np.log(g(x))', (0, 10), fontsize=12, color="blue")
    plt.annotate("- np.log(1 - g(x))", (.8, 10), fontsize=12, color="blue")
    plt.grid(True)
    plt.show()




test_g()
plot_cost_function()
