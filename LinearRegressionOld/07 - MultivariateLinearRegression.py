#  https://datatofish.com/multiple-linear-regression-python/
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
from scipy import stats



Stock_Market_df = pd.read_csv('D:\\myPython\\my_numpy\\Course-DataSciene\\SampleDataForMultivariateLinearRegression07.csv')
print(Stock_Market_df.head())

# Before you execute a linear regression model, it is advisable to validate that certain assumptions are met.
# you may want to check that a linear relationship exists between the dependent variable and the independent variable/s.
# In our example, you want to check that linear relationship exists between:
#
# The Stock_Index_Price (dependent variable) and the Interest_Rate (independent variable); and
# The Stock_Index_Price (dependent variable) and the Unemployment_Rate (independent variable)

plt.scatter(Stock_Market_df['Interest_Rate'], Stock_Market_df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.ylim(0)
plt.xlim(0)
plt.grid(True)
plt.show()

plt.scatter(Stock_Market_df['Unemployment_Rate'], Stock_Market_df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.ylim(0)
plt.xlim(0)
plt.grid(True)
plt.show()

# In the first case, when interest rates go up, the stock index price also goes up
# In the second case, when unemployment rates go up, the stock index price goes down
# (here we still have a linear relationship, but with a negative slope)

#  ##################################################################################################3
# with sklearn
# here we have 2 variables for multiple regression.
# If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.
# Alternatively, you may add additional variables within the brackets
# Y = C + M1*X1 + M2*X2 + ....
X = Stock_Market_df[['Interest_Rate','Unemployment_Rate']]
y = Stock_Market_df['Stock_Index_Price']
regressor = linear_model.LinearRegression()
regressor.fit(X, y)
print(X)
print('Intercept: ', regressor.intercept_)
print('Coefficients: ', regressor.coef_)


# prediction with sklearn
New_Interest_Rate = 2.75
New_Unemployment_Rate = 5.3
print('Predicted Stock Index Price:', regressor.predict([[New_Interest_Rate, New_Unemployment_Rate]]))
print("___________________________________________________________")

#  ##################################################################################################3
# with statsmodels
X = sm.add_constant(X)  # adding a constant
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
model_summary = model.summary()
print(model_summary)

# Y = C + M1*X1 + M2*X2 + ....
# Predicted_Stock_Index_Price = (const coef) + (Interest_Rate coef)*X1 + (Unemployment_Rate coef)*X2
Predicted_Stock_Index_Price = 1798.4040 + (345.5401 * 2.75) + (-250.1466 * 5.3)
print("Predicted_Stock_Index_Price = ", Predicted_Stock_Index_Price)
print("___________________________________________________________________")

