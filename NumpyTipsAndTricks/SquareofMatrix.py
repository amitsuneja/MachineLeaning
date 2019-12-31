import numpy as np

matrix_A = np.arange(1,7).reshape(2,3)
print("matrix_A=", matrix_A)

print(np.power(matrix_A, 2))
print((matrix_A)**2)
print(matrix_A*matrix_A)
