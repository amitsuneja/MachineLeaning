# Step 1 - Import the necessary libraries and the dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


my_dataset = pd.read_csv("D:\\myPython\\my_numpy\\Course-DataSciene\\SourceDataForMultivarietLinearRegression10.csv")
# print(my_dataset.head())
# print(my_dataset.describe())
# print(my_dataset.isnull().values.any())  # False if there is no null value and True if there is null value
# Note - above code will work only if there is null or blank value , But if there is
# amit or NAN instead of null or blank value then it wont detect that error.

# Step 2 - Plot the Seaborn Pairplot
sns.pairplot(my_dataset)
plt.show()

# Step 3 - Plot the Seaborn Heatmap
sns.heatmap(my_dataset.corr(), linewidth=0.2, vmax=1.0, square=True, linecolor='red', annot=True)
plt.show()

# Step 4 - Extract the Features and Labels
features = my_dataset.iloc[:, 0:-1].values
labels = my_dataset.iloc[:, -1].values

# Step 5 - Cross Validation (train_test_split)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=0)

# Step 6 - Create the Linear Model (LinearRegression)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Step 7 - Interpreting the Coefficient and the Intercept
y_pred = regressor.predict(X_test)

# Step 8 - Interpreting the Coefficient and the Intercept
print(regressor.coef_)
print(regressor.intercept_)

# Step 9 - Predict the Score (% Accuracy)
print('Train Score :', regressor.score(X_train, y_train))
print('Test Score:', regressor.score(X_test, y_test))

# Step 10- Verification of the Predicted Value
# y = b0 + b1*x1 + b2*x2 + b3*x3 + ... + bn*xn
y_output0 = regressor.intercept_ + regressor.coef_[0]*X_test[0][0] + regressor.coef_[1]*X_test[0][1] + regressor.coef_[2]*X_test[0][2] + regressor.coef_[3]*X_test[0][3]
y_output1 = regressor.intercept_ + regressor.coef_[0]*X_test[1][0] + regressor.coef_[1]*X_test[1][1] + regressor.coef_[2]*X_test[1][2] + regressor.coef_[3]*X_test[1][3]

# Step 11- Calculate the MSE(mean square error) and RMSE (root mean square error)
print('MSE :', metrics.mean_squared_error(y_test, y_pred))
print('RMSE :', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))







