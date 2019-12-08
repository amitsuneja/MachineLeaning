import numpy as np

"""
theta = inv(X^T * X) * X^T * y


If the determinant of the matrix is zero it will not have an inverse and your inv function will not work. 
This usually happens if your matrix is singular. But pinv will. This is because pinv returns the inverse of your matrix 
when it is available and the pseudo inverse when it isn't. 
The different results of the functions are because of rounding errors in floating point arithmetic"""


MATRIX_A = np.array([[1, 2, 3], [1, 3, 3], [1, 2, 4]])
Inv_MATRIX_A = np.linalg.inv(MATRIX_A)
Sudo_Inv_MATRIX_A = np.linalg.pinv(MATRIX_A)
print("Matrix A = ")
print(MATRIX_A)

print("Inverse Of Matrix A =")
print(Inv_MATRIX_A)


print("np.dot(Matrix A, Inv_MATRIX_A) =")
print(np.dot(MATRIX_A, Inv_MATRIX_A))
print("_____________________________________________________")

print("SUDO - Inverse Of Matrix A =")
print(Sudo_Inv_MATRIX_A)

print("np.dot(Matrix A, Sudo_Inv_MATRIX_A) =")
print(np.dot(MATRIX_A, Sudo_Inv_MATRIX_A))

