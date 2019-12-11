"""  https://www.kaggle.com/rakend/multiple-linear-regression-with-gradient-descent  """
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np

# you generate theta randomly , so every time it should give same result.
np.random.seed(10)


def gradient_descent(X, Y, m, theta, alpha):
    cost_list = []  # to record all cost values to this list
    theta_list = []  # to record all theta_0 and theta_1 values to this list
    prediction_list = []
    run = True
    cost_list.append(1e10)  # we append some large value to the cost list
    i = 0
    while run:
        prediction = np.dot(X, theta)  # predicted y values theta_0*x0+theta_1*x1
        prediction_list.append(prediction)
        my_error = prediction - Y
        cost = 1 / (2 * m) * np.dot(my_error.T, my_error)  # (1/2m)*sum[(error)^2]
        cost_list.append(cost)
        theta = theta - (alpha * (1 / m) * np.dot(X.T, my_error))  # alpha * (1/m) * sum[error*x]
        theta_list.append(theta)
        if cost_list[i] - cost_list[i + 1] < 1e-9:  # checking if the change in cost function is less than 10^(-9)
            run = False
        print("Iteration number {} have cost = {}".format(i, cost))
        i += 1
    cost_list.pop(0)  # Remove the large number we added in the begining
    return prediction_list, cost_list, theta_list


def create_boston_df():
    boston = datasets.load_boston()
    print(boston.keys())
    df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
    df['target'] = boston.target
    my_dict = {"target": "Price"}
    df = df.rename(columns=my_dict)
    return df


df = create_boston_df()
# This two lines expains correlation between variables , i.e which variable we need to select
correlation = df.corr(method='pearson')
print(correlation['Price'].abs().sort_values(ascending=False))  # Price is highly correlated to LSTAT and RM

X_RM = df['RM']
X_L_STAT = df['LSTAT']
X_PTRATIO = df['PTRATIO']
Y = df['Price']

# Plotting a Figure after scaling of data
plt.scatter(Y, X_RM, s=5, color="green", label='RM')
plt.scatter(Y, X_L_STAT, s=5, color="red", label='LSTAT')
plt.scatter(Y, X_PTRATIO, s=5, color="blue", label='X_PTRATIO')
plt.legend(fontsize=15)
plt.xlabel('Average number of rooms & Low status population', fontsize=15)
plt.ylabel('Price', fontsize=15)
plt.legend()
plt.savefig("MultiLinearRegressionWithGradientDescent-Before.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window

# Scaling the data
X_RM = preprocessing.scale(df['RM'])
X_L_STAT = preprocessing.scale(df['LSTAT'])
X_PTRATIO = preprocessing.scale(df['PTRATIO'])
Y = preprocessing.scale(df['Price'])

# Plotting a Figure after scaling of data
plt.scatter(Y, X_RM, s=5, color="green", label='RM')
plt.scatter(Y, X_L_STAT, s=5, color="red", label='LSTAT')
plt.scatter(Y, X_PTRATIO, s=5, color="blue", label='X_PTRATIO')
plt.legend(fontsize=15)
plt.xlabel('Average number of rooms & Low status population', fontsize=15)
plt.ylabel('Price', fontsize=15)
plt.legend()
plt.savefig("MultiLinearRegressionWithGradientDescent-After.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window

# Lets Create a Matrix to do calculation
X = np.c_[np.ones(X_RM.shape[0]), X_L_STAT, X_RM, X_PTRATIO]

# Required Parameters for Gradient decent
alpha = 0.0001  # is learning rate
m = X.shape[0]  # no. of samples
theta = np.random.rand(X.shape[1])  # theta_0*x0+theta_1*x1+............

# calling Gradient Decent
prediction_list, cost_list, theta_list = gradient_descent(X, Y, m, theta, alpha)
theta = theta_list[-1]

# Using equation y = theta_0*x0+theta_1*x1+............as we know what is theta correct value
YP = theta[0]
for i in range(1, X.shape[1]):
    YP = YP + theta[i] * X[:, i]

# MeanSquare error
MSE_equ = ((YP - Y) ** 2).mean()  # Using YP from equation of hyperplane
MSE_GD = ((prediction_list[-1] - Y) ** 2).mean()  # From Gradient Descent

print('Mean Square Error using equation of hyperplane : {}'.format(round(MSE_equ, 3)))
print('Mean Square Error from Gradient Descent prediction : {}'.format(round(MSE_GD, 3)))

# Drawing a cost function
plt.title('Cost Function J', size=30)
plt.xlabel('No. of iterations', size=20)
plt.ylabel('Cost', size=20)
plt.plot(cost_list)
plt.savefig("MultiLinearRegressionWithGradientDescent-CostFunction.png")
plt.cla()  # Clear axis
plt.clf()  # Clear figure
plt.close()  # Close a figure window

print('Intercept : {}'.format(round(theta[0], 3)))
print('Theta_0 : {}'.format(round(theta[1], 4)))
print('Theta_1 : {}'.format(round(theta[2], 4)))

r2 = 1 - (sum((Y - prediction_list[-1]) ** 2)) / (sum((Y - Y.mean()) ** 2))
print('R square doing from the scratch: {}'.format(round(r2, 4)))
