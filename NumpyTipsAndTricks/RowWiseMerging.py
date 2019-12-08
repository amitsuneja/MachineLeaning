import numpy as np

V = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([7, 8, 9, 10, 11, 12])
print(np.r_[V[0:2], Y[0], V[3], Y[1:3], V[4:], Y[4:]])
