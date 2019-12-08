# Polynomial Linear Regression

# Step 1  - Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step2 - Read the data into pandas data frame and extract X and y values from dataframe
my_data_set = pd.read_csv("DataForPolynomialRegression.csv")
print(type(my_data_set))
print(my_data_set)
X = my_data_set.iloc[:, 1:2].values
print(X)
y = my_data_set.iloc[:, 2].values
print(y)


# Step 3 - Lets plot the data we have to see how it looks.
plt.scatter(X, y, color='red', label='What regression i should use? Just rought idea')
plt.xlabel('Level/Rank')
plt.ylabel('Salary')
plt.show()


# step 3 - lets find value of X in polynomial regression  when degree=3
# Do not use very high degree , else you might be over fitting.
my_polynomial_regression = PolynomialFeatures(degree=3)
X_my_polynomial_regression = my_polynomial_regression.fit_transform(X)
print(X_my_polynomial_regression)


# Step 4 - Lets use the data and give training to our model (named as regressor)
regressor = LinearRegression()
regressor.fit(X_my_polynomial_regression, y)

# Step 5 - Lets plot the regression.
plt.scatter(X, y, color='red', label='Polynomial Liner Regression')
plt.plot(X, regressor.predict(X_my_polynomial_regression))
plt.xlabel('Level/Rank')
plt.ylabel('Salary')
plt.show()

# Step8 - Now append value 12,14,15,22 to array X and predict value of y
X_to_append = np.array([[12], [14], [15], [22]])
X_new = np.concatenate((X, X_to_append))
X_my_polynomial_regression_new = my_polynomial_regression.fit_transform(X_new)
X_my_polynomial_regression_to_append = my_polynomial_regression.fit_transform(X_to_append)
y_to_append = regressor.predict(X_my_polynomial_regression_to_append)


print(X_to_append)
print(X_my_polynomial_regression_to_append)
print(y_to_append)

# Step 9 - Lets plot the regression.
plt.scatter(X, y, color='red', label='Given Data')
plt.scatter(X_to_append, y_to_append, color='green', label='Predicted Data')
plt.plot(X_new, regressor.predict(X_my_polynomial_regression_new))
plt.xlabel('Level/Rank')
plt.ylabel('Salary')
plt.show()




















