import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Below 2 lines is just to show how to print float in python3.
my_float_var = 1.1311111
print("{0:.2f}".format(my_float_var))
print("________________________________")
array = np.random.rand(5)
print(array)
print("________________________________")

# Below we are creating Normal(Gaussian) Distribution , This is Distribution is also known as Bell Curve
# numpy.random.normal(loc = 0.0, scale = 1.0, size = None) ,
# loc   : [float or array_like]Mean of the distribution.
# scale : [float or array_like]Standard Derivation of the distribution.
# size  : [int or int tuples].
# 0.0 is mean of distribution and 1.0 is standard deviation of the distribution
array = np.random.normal(0, 1, 5)
print(array)
print(array.mean())
print(np.median(array))
print("________________________________")


# Lets take example
incomes = np.random.normal(27000, 15000, 10000)
print(type(incomes))
print("Mean of Incomes = {}".format(np.mean(incomes)))  # 2 syntax to print mean np.mean(array_variable) and array_variable.mean
print("Median of Incomes = {}".format(np.median(incomes)))
print("________________________________")
# We can segment the income data which is 10K different values into 50 buckets, and plot it as a histogram:
plt.hist(incomes, 50)
plt.show()
# Now we will add and a very high income into the mix. Darn income inequality!
incomes = np.append(incomes, [1000000000000000])
print("Mean of Incomes = {}".format(np.mean(incomes)))
print("Median of Incomes = {}".format(np.median(incomes)))
print("________________________________")
# You can see above 2 outpput of mean and medians , How mean value get changed by adding one high income.
# Thats is why you always need to consider median in stats.


# # Lets do mode example using scipy
ages = np.random.randint(18, high=90, size=500)
print(ages)
print(stats.mode(ages))
print("Mean of ages ={}".format(ages.mean()))
print("Median of ages ={}".format(np.median(ages)))


