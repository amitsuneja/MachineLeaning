import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
print(type(pageSpeeds))
print(type(purchaseAmount))

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

# numpy has a handy polyfit function we can use, to let us construct an nth-degree polynomial
# model of our data that minimizes squared error. Let's try it with a 4th degree polynomial:

X = np.array(pageSpeeds)
y = np.array(purchaseAmount)
p4 = np.poly1d(np.polyfit(X, y, 4))
print(X.shape)
print(y.shape)
print(type(p4))

# We'll visualize our original scatter plot, together with a plot of our predicted values using
# the polynomial for page speed times ranging from 0-7 seconds:

xp = np.linspace(0, 7, 100)
plt.scatter(X, y)
plt.plot(xp, p4(xp), color='red')
plt.show()

# Looks pretty good! Let's measure the r-squared error:
r2 = r2_score(y, p4(X))
print(r2)


