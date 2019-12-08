import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_datafile(filename):
    """
    Function to read the data file.

    :param filename: name of file to convert to panda dataframe
    :return: dataframe
    """
    try:
        f = open(filename)
    except IOError:
        print("File not accessible")
    finally:
        f.close()

    try:
        data = pd.read_csv(filename, header=None)   # if csv file have header then remove this header option
        data.columns = ["chip_test1", "chip_test2", "result"]
        """ Result column :  0 means the chip has been rejected and 1 means accepted."""
        return data
    except:
        print("unable to read file")


def visual_pre_data_processing(df):
    """
    While touching your data it is always a good idea to view your data in scatter plot. this will always help you.
    this function simply plot data in scatter plot.
    Also i realised after viewing graph that i dont have to normalize or standrdize this data.

    :param df: dataframe containing data
    :return: None
    """
    print("Dimension of matrix in pre data processing: {}".format(df.shape))
    mask_pass = df["result"] == 1
    mask_fail = df["result"] == 0
    passed = plt.scatter(df[mask_pass]['chip_test1'].values, df[mask_pass]['chip_test2'].values, c="green")
    failed = plt.scatter(df[mask_fail]['chip_test1'].values, df[mask_fail]['chip_test2'].values, c="red")
    plt.legend((passed, failed), ('Passed green', 'Failed red'))
    plt.xlabel("chip_test1")
    plt.ylabel("chip_test2")
    # plt.show()
    plt.savefig("PolynomialMicroChipTesting-visual_pre_data_processing.png")
    plt.cla()    # Clear axis
    plt.clf()    # Clear figure
    plt.close()  # Close a figure window


def split_features_and_result(df):
    """
    This function simply read split the dataframe into 2 dataframes.
    df_X - will have your all the features.
    df_y - will have result.

    :param df: dataframe to split
    :return: df_X and df_y
    """
    df_X = df.iloc[:, 0:2]
    df_y = df.iloc[:, -1:]
    return df_X, df_y


def feature_mapping(df):
    """
    This function is doing feature mapping because we need to convert function into polynomial function.

    :param df: dataframe whose dimention you want to increase
    :return: result which is data frame that fit to polynomial function.
    """
    from sklearn.preprocessing import PolynomialFeatures
    my_poly = PolynomialFeatures(6)
    result = my_poly.fit_transform(df)
    print("Current Dimensions of matrix after feature mapping = {}".format(result.shape))
    return result


def sigmoid(x):
  return 1/(1+np.exp(-x))




df = read_datafile("PolynomialExample.txt")
visual_pre_data_processing(df)
df_X, df_y = split_features_and_result(df)
result = feature_mapping(df_X)
