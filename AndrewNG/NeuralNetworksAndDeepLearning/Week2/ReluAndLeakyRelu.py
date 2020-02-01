# plot inputs and outputs
from matplotlib import pyplot as plt

"""
RELU :      f(x) = max(0,x) 

LEAKY RELU: f(x) = x if x > 0 and f(x) = 0.01x if x <= 0. 
"""

# rectified linear function


def relu(x):
    return max(0.0, x)


def leaky_relu(x):
    if x > 0:
        return x
    else:
        return 0.01 * x

# relu example
# define a series of inputs
series_in = [x for x in range(-10, 11)]
# calculate outputs for our inputs
series_out = [relu(x) for x in series_in]
# line plot of raw inputs to rectified outputs
plt.plot(series_in, series_out)
plt.show()

# Leaky relu example
# define a series of inputs
series_in = [x for x in range(-10, 11)]
# calculate outputs for our inputs
series_out = [leaky_relu(x) for x in series_in]
# line plot of raw inputs to rectified outputs
plt.plot(series_in, series_out)
plt.show()

