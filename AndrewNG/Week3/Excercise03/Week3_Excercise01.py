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
import scipy.optimize as opt


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


def fit_x(df_x, df_y):
    x = np.c_[np.ones(df_x.shape[0]), df_x]
    theta = np.zeros((x.shape[1], 1))
    y = df_y.to_numpy()
    return x, y, theta


def z(x, theta):
    return np.dot(x, theta)


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))  # note outer brackets in denominator are important else it bad/wrong result.


def cost_function(theta, x, y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    j = (1/m) * np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h), axis=0)
    return j


def cost_function1(theta, x, y):
    """
    You can see we have implemented cost function twice.
    cost_function and cost_function1: Basically both do same job but way of implementation is different.
    cost_function - uses np.sum on outside and np.multiply to matrix
    cost_function1 - uses as np.dot to multiply to matrix and np.sum is not required.
    I hope you know why ?
    Here is output of both function when i initialized by theta and calculated cost :
    temp_cost using cost_function = [[0.69314718]]
    temp_cost1 using cost_function1 = [[0.69314718]]

    Tip1 : remember cost function should always return single value or matrix of 1x1
    if you are getting more then one values then you have problem.

    np.dot(np.log(h), -y.T) - np.dot(np.log(1 - h), (1 - y).T) this is incorrect implementation.
    or
    np.dot(-y , np.log(h).T) - np.dot((1 - y), np.log(1 - h).T) this is incorrect implementation/


    Tip2: Derivative of your cost function will always return matrix.
    If you have 3 thetas , then it will return matrix of 3X1 or 1X3 depending on shape of data.

    """
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    j = (1/m) * (np.dot(np.log(h).T, -y) - np.dot(np.log(1 - h).T, (1 - y)))
    return j


def first_deri_j(theta, x, y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    calculation = (1/m) * (np.dot((h - y).T, x))
    return calculation.T


def first_deri_j1(theta , x , y):
    m = x.shape[0]
    h = sigmoid(z(x, theta))
    calculation = 1/m * np.sum((h-y)*x, axis=0)
    return calculation

def get_best_theta_using_scipy_lib(cost_func_name, theta, first_deri_of_cost_func, x , y):
    """
    Note on flatten() function: Unfortunately scipy’s fmin_tnc doesn’t work well with column or row vector.
    It expects the parameters to be in an array format. The flatten() function reduces a column or row vector
    into array format.
    """
    temp = opt.fmin_tnc(func=cost_func_name,
                        x0=theta.flatten(),
                        fprime=first_deri_of_cost_func,
                        args=(x, y.flatten()))
    return temp


def grad_desc(x, y, theta, lr=.01, converge_change=0.001):
    cost_list = list()
    cost_list.append(1e10)
    i = 0
    run = True
    while run:
        theta = theta - lr * first_deri_j(theta, x, y)
        cost = cost_function(theta, x, y)
        cost_list.append(cost)
        # print("Value of i = {} and i+1 ={}".format(i, i+1))
        # print("cost[{}] = {} and cost[{}] = {}".format(i, cost_list[i], i+1, cost_list[i+1]))
        # print("cost_list[{}] - cost_list[{}] = {} ".format(i, i+1, cost_list[i] - cost_list[i + 1] ))
        if cost_list[i] - cost_list[i + 1] < converge_change:
            run = False
        i += 1
    cost_list.pop(0)
    return theta, i, cost_list


def only_for_troubleshooting(x, theta, y, cost_function, first_deri_j):
    pass
    Z = z(x, theta)
    # print("Z =", Z)
    # print("Z.shape=", Z.shape)
    hypothesis = sigmoid(Z)
    # print(hypothesis.shape)
    print(hypothesis)
    print(sigmoid(0))    # should display .5 then your sigmoid is perfect
    temp_cost = cost_function(theta, x, y)
    print("temp_cost using cost_function =", temp_cost)
    # temp_cost1 = cost_function1(theta, x, y)
    # print("temp_cost1 using cost_function1 =", temp_cost1)
    # print("we did not print temp_cost1.shape as it is scaler number not vector")
    # print("Did you notice that both implementations of cost function produce same result")
    derivative = first_deri_j(theta, x, y)
    print(derivative)
    # derivative1 = first_deri_j1(theta, x, y)
    # print(derivative1)



if __name__ == "__main__":
    df = read_data_file("ex2data1.txt")
    df_x, df_y = segregate_x_y(df)
    df_x_pass, df_x_fail = segregate_x_into_pass_fail(df_x, df_y)
    plt = plot_pass_fail(df_x_pass, df_x_fail)
    x, y, theta = fit_x(df_x, df_y)
    #only_for_troubleshooting(x, theta, df_y,cost_function,first_deri_j)
    theta_optimized = get_best_theta_using_scipy_lib(cost_function, theta, first_deri_j, x , y)
    theta_optimized = theta_optimized[0]
    print("Auto theta optimized =", theta_optimized)
    theta, i, cost_list = grad_desc(x, y, theta)
    print("Manual theta optimized =",theta)












