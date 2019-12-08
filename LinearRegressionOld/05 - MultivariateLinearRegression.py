# MultivariateLinearRegression
# Sample problem of predicting home price in monroe, new jersey (USA)
# Below is the table containing home prices in monroe twp, NJ. Here price depends on area (square feet),
# bed rooms and age of the home (in years).
# Given these prices we have to predict prices of new homes based on area, bed rooms and age.

import pandas as pd
import numpy as np
from sklearn import linear_model
import math


# Read the CSV file and create a data frame
my_data_frame = pd.read_csv('SourceDataForMultivarietLinearRegression09.csv')

# print the data frame and see the NAN value in it .
print(my_data_frame)

# Lets calculate the median
med_bedrooms = math.floor(my_data_frame.bedrooms.median())
# print the median for our reference
print(med_bedrooms)

# Lets fill NaN with the median value
my_data_frame.bedrooms = my_data_frame.bedrooms.fillna(med_bedrooms)

# print the data frame and see the NAN is replaced by median.
print(my_data_frame)

# Lets create the regression object which is our model.
regressor = linear_model.LinearRegression()


# Lets train the regression model object with the data .
# Below 'area', 'bedrooms', 'age' are given and we have to predict price.
regressor.fit(my_data_frame[['area', 'bedrooms', 'age']], my_data_frame.price)


# what are our coefficients value. (means value of m1, m2 and m3 in equation.
print(regressor.coef_)

# what is value of intercept (means value of b in the equation)
print(regressor.intercept_)

# Find price of home with 3000 sqr ft area, 3 bedrooms, 40 year old
print("Value of home1 = ", regressor.predict([[3000, 3, 40]]))
# lets validate that predicted value is ok  or not.
print(112.06244194*3000 + 23388.88007794*3 - 3231.71790863*40 + 221323.00186540384)

# Find price of home with 2500 sqr ft area, 4 bedrooms, 5 year old
print("Value of home2 = ", regressor.predict([[2500, 4, 5]]))
# lets validate that predicted value is ok  or not.
print(112.06244194*2500 + 23388.88007794*4 - 3231.71790863*5 + 221323.00186540384)

# Find price of home with 3500 sqr ft area, 3 bedrooms, 30 year old
print("Value of home3 = ", regressor.predict([[3600, 3, 30]]))
# lets validate that predicted value is ok  or not.
print(112.06244194*3600 + 23388.88007794*3 - 3231.71790863*30 + 221323.00186540384)









