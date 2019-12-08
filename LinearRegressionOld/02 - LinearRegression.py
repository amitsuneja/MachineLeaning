##################################################################################################################
# Linear regression assumes a linear or straight line relationship between the input variables (X)
# and the single output variable (y).
# Here X is independent variable and y is dependent variable.
#
# y(cap) = b0 + b1*x --->  (y = mx+ c )  y is dependent variable , m is slope and  c is intercept
# b0 is intercept and b1 is slope( and remember y is not y is mean of possible y i.e y(cap))
# where b0 and b1 are the coefficients we must estimate from the training data.
# B1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
# B0 = mean(y) - B1 * mean(x)
#################################################################################################################

##################################################################################################################
# Training - color='red', label='training data'
# Test - color='green', label='test data'
# Prediction - color='blue', label='Predicted data'
# fitline - color='magenta', label='fit line'
#################################################################################################################
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats


# Step1 - Open and Read the CSV File
my_data_set = pd.read_csv("SourceDataForLinearRegression.csv")
X = my_data_set.iloc[:, :-1].values
y = my_data_set.iloc[:, 1].values


# print(X.view())  # view your array
print(X.shape)   # notice shape of array 1D or 2D or 3D
print(y.shape)
print("_____________________________________")
print(X.dtype)   # Check for data type if array float or int
print(y.dtype)
# X all are int type and y is float type.
print("_____________________________________")
print(X.size)    # what is size of array
print(y.size)
print("_____________________________________")
print(X.ndim)    # notice shape of array 1D or 2D or 3D
print(y.ndim)
# Note : We created X as Two dimensional array and y as one dimensional array . We did it by using a :-1 and 1 in
# .iloc
print("_____________________________________")
print(X.view())
print(y.view())


# Step 2 - Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
# test_size - we are saying that make 1/3 data as training data (test 21 records + train 42 records = 63 records)
print("_____________________________________")
# print(X_train)
print(X_train.size)
print(X_test.size)
print(y_train)
print(y_train.size)
print(y_test.size)
print("_____________________________________")

# Step3- Visualising the Training set Data and decide your regression model/algorithm we can use.
plt.scatter(X_train, y_train, color='red', label='training data')
plt.xlabel('NumberOfClaims')
plt.ylabel('PaymentForAllTheClaims')
plt.legend()
plt.show()
# From this diagram we realised that this data is fit for Liner Regression.(Means a straight line can be drawn with
# min error)


# Step4- Lets use the train data and give training to our model (named as regressor)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step5- Visualising the Training set results
plt.scatter(X_train, y_train, color='red', label='training data')
plt.plot(X_train, regressor.predict(X_train), color='magenta', label='fit line')
plt.xlabel('NumberOfClaims')
plt.ylabel('PaymentForAllTheClaims')
plt.legend()
plt.show()

# Step6- Visualizing the Test Set result
plt.scatter(X_test, y_test, color='green', label='test data')
plt.scatter(X_train, y_train, color='red', label='training data')
plt.plot(X_test, regressor.predict(X_test), color='magenta', label='fit line')
plt.xlabel('NumberOfClaims')
plt.ylabel('PaymentForAllTheClaims')
plt.legend()
plt.show()


# Step7 - Now append value 140,145,160,165 and 185 to array X and predict value of y

X_to_append = np.array([[140], [157], [175], [166], [200]])

print(X_to_append)
print(X.shape)   # notice shape of array 1D or 2D or 3D
print(X_to_append.shape)   # notice shape of array 1D or 2D or 3D

X_new = np.concatenate((X, X_to_append))

y_to_append = regressor.predict(X_to_append)
print(y_to_append)
print(y.shape)   # notice shape of array 1D or 2D or 3D
print(y_to_append.shape)   # notice shape of array 1D or 2D or 3D

y_new = np.concatenate((y, y_to_append))

# Step8 - Lets Visualize the Complete Data (Training + Test + predicted)
plt.scatter(X_train, y_train, color='red', label='training data')
plt.scatter(X_test, y_test, color='green', label='test data')
plt.scatter(X_to_append, y_to_append, color='blue', label='Predicted data')
plt.plot(X_new, regressor.predict(X_new), color='magenta', label='fit line')
plt.xlabel('NumberOfClaims')
plt.ylabel('PaymentForAllTheClaims')
plt.legend()
plt.show()
print("____________________________________")


print(X.shape)   # notice shape of array 1D or 2D or 3D
print(y.shape)
print("_____________________________________")
print(X.size)    # what is size of array
print(y.size)
print("_____________________________________")
X_reshaped = X.reshape(63)
print(X.shape)   # notice shape of array 1D or 2D or 3D
print(X_reshaped.shape)
print(y.shape)
print("_____________________________________")

slope, intercept, r_value, p_value, std_err = stats.linregress(X_reshaped, y)
print("r-squared i.e coefficient of determination (Tip : 0 -> Bad , 1 -> Good) :", r_value**2)
print("slope = {}".format(slope))
print("intercept={}".format(intercept))
print("p_value={}".format(p_value))
print("std_err={}".format(std_err))
print("slope : float - slope of the regression line")
print("intercept : float - intercept of the regression line")
print("r_value : float - correlation coefficient")
print("p_value : float - two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero, "
      "using Wald Test with t-distribution of the test statistic.")
print("stderr : float - Standard error of the estimated gradient i.e it means how well the data points fits around the"
      "regression line.")







