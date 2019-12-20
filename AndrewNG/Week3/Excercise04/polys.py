import numpy as np
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(6, 1)
print(X)

poly = PolynomialFeatures(3)
print(poly.fit_transform(X))
print(poly.fit_transform(X).shape)


X = X.reshape(1, 6)
print(X)
poly = PolynomialFeatures(3)
print(poly.fit_transform(X))
print(poly.fit_transform(X).shape)



