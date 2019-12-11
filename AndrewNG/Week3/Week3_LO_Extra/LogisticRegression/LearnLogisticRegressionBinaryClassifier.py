import numpy as np  # Numerical computing
import matplotlib.pyplot as plt  # plotting core


def g(z):
    return 1/(1 + np.exp(-z))


def generate_data():
    return np.linspace(-10, 10, 100)


def test_g():
    z = generate_data()
    plt.plot(z, g(z))
    plt.grid(True)
    plt.xlabel("z")
    plt.ylabel("Sigmoid(z)")
    plt.annotate('Convex', (-7.5, 0.2), fontsize=18)
    plt.annotate('Concave', (3, 0.8), fontsize=18)
    plt.title("Sigmoid Function g(z) = 1/(1 + exp(-z))", fontsize=12, color="blue")
    plt.show()
    return plt


def plot_cost_function():
    x = generate_data()
    plt.plot(g(x), -np.log(g(x)))
    plt.plot(g(x), -np.log(1-g(x)))
    plt.xlabel("g(x)", fontsize=12, color="blue")
    plt.ylabel("cost", fontsize=12, color="blue")
    plt.annotate('- np.log(g(x))', (0, 10), fontsize=12, color="blue")
    plt.annotate("- np.log(1 - g(x))", (.8, 10), fontsize=12, color="blue")
    plt.grid(True)
    plt.show()
    return plt


if __name__ == "__main__":
    # plt = test_g()
    # plt.show()
    plt = plot_cost_function()
    plt.show()




