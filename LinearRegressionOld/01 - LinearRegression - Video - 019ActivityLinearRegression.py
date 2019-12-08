import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def predict(x):
    return slope * x + intercept


pageSpeeds = np.random.normal(3.0, 1.0, 10)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 10)) * 3
print(pageSpeeds)
print(purchaseAmount)


slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
"""slope : float - slope of the regression line
intercept : float - intercept of the regression line
r_value : float - correlation coefficient
p_value : float - two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero, 
using Wald Test with t-distribution of the test statistic.
stderr : float - Standard error of the estimated gradient."""


print("Slope = {}".format(slope))
print("Intercept={}".format(intercept))
print("r_value={}".format(r_value))
print("p_value={}".format(p_value))
print("std_error={}".format(std_err))

print("How  good out Liner Regression is R**2 = {} (Tip : 0 -> Bad , 1 -> Good)".format(r_value ** 2))

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount, color='green', label="my Data points")
plt.plot(pageSpeeds, fitLine, color='orange', label='fitted line')
plt.legend()
plt.show()

