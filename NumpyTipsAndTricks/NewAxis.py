import numpy as np
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([5, 4, 3])
print(x1)
print(x2)
x1 = x1[:, np.newaxis]
print(x1)
print(x1 + x2)