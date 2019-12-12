"""
Problem context
Suppose that you are the administrator of a university department and you want to determine each applicant’s
chance of admission based on their results on two exams. You have historical data from previous applicants that
you can use as a training set for logistic regression. For each training example, you have the applicant’s scores
on two exams and the admissions decision.

Your task is to build a classification model that estimates an applicant’s probability of admission based on
the scores from those two exams.

Data - ex2data1.txt

Format of Data:-
Exam1Score,Exam2Score,0or1 -> Here 0 means candidate was unable to get an admission and 1 vice-versa.

Note : this code uses df.to_numpy which introduced in pandas 0.25.3 so make sure you panda is updated.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


def read_data_file(filemame):
    df = pd.read_csv(filemame, header=None)
    df.columns = ["Exam1Score", "Exam2Score", "AdmitORNot"]
    return df


def segregate_x_y(df):
    df_x = df[["Exam1Score","Exam2Score"]]  # single [] gives error in this case
    df_y = df[["AdmitORNot"]]  # if i put single [] then it return series and [[]] return dataframe
    return df_x, df_y


def segregate_x_into_pass_fail(df_x, df_y):
    mask_pass = df_y["AdmitORNot"] == 1
    df_x_pass = df_x[mask_pass]
    df_x_fail = df_x[~mask_pass]
    return df_x_pass, df_x_fail


def plot_pass_fail(df_x_pass, df_x_fail):
    plt.scatter(df_x_pass["Exam1Score"], df_x_pass["Exam2Score"],marker="o",color="green",label="Admitted")
    plt.scatter(df_x_fail["Exam1Score"], df_x_fail["Exam2Score"],marker="o",color="red",label="Not Admitted")
    plt.xlabel("Exam1 Score")
    plt.ylabel("Exam2 Score")
    plt.legend(loc="best")
    return plt


def fit_x(df_x):
    x = np.c_[np.ones(df_x.shape[0]), df_x]
    theta = np.zeros((x.shape[1], 1))
    return x, theta


def z(x, theta):
    return np.dot(x, theta)


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))  # note outer brackets in denominator are important else it bad/wrong result.


def cost_function(theta, x, y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    j = (1/m) * np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h))
    j = j[:, np.newaxis]  # if we don't need this step we will check it later.
    return j


def cost_function1(theta, x, y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    j = (1/m) * (np.dot(np.log(h).T, -y) - np.dot(np.log(1 - h).T, (1 - y)))
    return j


def first_deri_j(theta, x, y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    calculation = (1/-m) * (np.dot((h - y).T, x))
    return calculation.T






"""

this is incorrect implementation as this gives a scaler output where as about output gives matrix 
1, 3 which we transposed to 3,1 and returned .

# def first_deri_j(theta , x , y):
#     m = x.shape[0]
#     h = sigmoid(z(x, theta))
#     y = y.to_numpy()
#     calculation = 1/m * (np.sum(((h-y)*x)))
#     print(calculation)
"""

def only_for_troubleshooting(x, theta, y):
    pass
    # Z = z(x, theta)
    # print("Z =", Z)
    # print("Z.shape=", Z.shape)
    # hypothesis = sigmoid(Z)
    # print(hypothesis.shape)
    # print(hypothesis)
    print(sigmoid(0))    # should display .5 then your sigmoid is perfect
    temp_cost = cost_function(theta, x, y)
    print("temp_cost using cost_function =", temp_cost)
    temp_cost1 = cost_function1(theta, x, y)
    print("temp_cost1 using cost_function1 =", temp_cost1)
    print("we did not print temp_cost1.shape as it is scaler number not vector")
    print("Did you notice that both implementations of cost function produce same result")

    # derivative = first_deri_j(theta, x, y)
    # print(derivative)


if __name__ == "__main__":
    df = read_data_file("ex2data1.txt")
    df_x, df_y = segregate_x_y(df)
    df_x_pass, df_x_fail = segregate_x_into_pass_fail(df_x, df_y)
    plt = plot_pass_fail(df_x_pass, df_x_fail)
    x, theta = fit_x(df_x)
    only_for_troubleshooting(x, theta, df_y)










