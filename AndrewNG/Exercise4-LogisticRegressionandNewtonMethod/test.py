"""

https://www.dotnetlovers.com/article/225/logistic-regression-explained
"""
import numpy as np
import math
from sklearn import datasets
from sklearn.model_selection import train_test_split

class LogisticRegression:
    def __init__(self, X):
        self.beta_old_i = []
        # initializing b_i, always one additional coefficient than number of features of predictor
        # because eq β_0 + β_1*x having two coefficients β_0, β_1 where x has only one dimension
        self.beta_new_i = np.zeros(X.shape[1] + 1)

    # p(x) = e^(β_0 + β_1*x)/(1 + e^(β_0 + β_1*x))
    def probabilityFun(self, X):
        z = np.dot(self.beta_new_i, X.T)
        p = math.e ** z / (1 + math.e ** z)
        return p

    # f'(β_j) = dl/d(β_j) = (i=1 to N)_Σ (y_i - p(x_i))*x_ij
    def firstDerivative(self, X, Y, P):
        firstDer = np.dot((Y - P), X)
        return firstDer

    # f''(β_k) = dl/d(β_j)d(β_k) = - (i=1 to N)_Σ x_ij*x_ik*p(x_i)*(1 - p(x_i))
    def secondDerivative(self, X, P):
        probMul = P * (1 - P)
        xMulp = np.array([x * y for (x, y) in zip(X, probMul)])
        secondDer = -1 * np.dot(xMulp.T, X)
        return secondDer

    # β_(i+1) = β_i - (f'(β_i))/(f''(β_i))
    def newtonRaphson(self, firstDer, secondDer):
        self.beta_new_i = self.beta_old_i - np.dot(np.linalg.inv(secondDer), firstDer)


    # training the model
    def fit(self, X, Y, maxIteration=50, diffThreshHold=10 ** -5):
        # adding one additional column since we will have additional coefficient
        X = np.c_[X, np.array([1] * X.shape[0])]
        iteration = 0
        diffBetaList = []

        while (list(self.beta_new_i) != list(self.beta_old_i)):
            self.beta_old_i = self.beta_new_i
            P = self.probabilityFun(X)
            firstDer = self.firstDerivative(X, Y, P)
            secondDer = self.secondDerivative(X, P)
            self.newtonRaphson(firstDer, secondDer)
            # difference between last calcuated coefficients and current coefficients
            diff = np.linalg.norm(self.beta_new_i - self.beta_old_i)
            diffBetaList.append(diff)
            iteration += 1
            if (diff <= diffThreshHold or iteration > maxIteration):
                break

        return diffBetaList

    #predict probability any new data points
    def predict(self, X):
        X = np.c_[X, np.array([1]*X.shape[0])]
        probability = self.probabilityFun(X)
        return probability

    #classify based on provided classes
    def classify(self, X, dataClass):
        Y = self.predict(X)
        #if probability is less than 0.5 than categorized as class one else class two
        return [0 if item <= 0.05 else 1 for item in Y]

iris = datasets.load_iris()
#iris data is 50 each three classes so only taking to 100 for two classes
x_train, x_test, y_train, y_test = train_test_split(iris['data'][:100], iris['target'][:100])
reg = LogisticRegression(x_train)
reg.fit(x_train,y_train)
pred = reg.classify(x_test, iris["target_names"][:2])
print("Accuracy: {:.2f}%".format(100*np.mean(pred == y_test)))
