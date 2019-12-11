import numpy as np
a = 5
b = 6

c = np.ones((2, 1))
print(c)
c[0][0] = a
c[1][0] = b
print(c)
