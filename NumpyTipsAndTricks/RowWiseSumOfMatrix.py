import numpy as np

matrix = np.array([[56.0, 0.0, 4.4, 68.0], [1.2, 104.0, 52.0, 8.0], [1.8, 135.0, 99.0, 0.9]])
print("Question :Given Data Table:")
print(matrix)
print(" You have been asked to calcuate row wise percentage???")
print("")
print("Solution:")
print("")
sum_of_rows = matrix.sum(axis=0)
print("Row Wise sum of all elements:",sum_of_rows)
print("")
print(" Now Percent is as given below:")
percent_matrix = 100*(matrix / sum_of_rows)
print(percent_matrix)


