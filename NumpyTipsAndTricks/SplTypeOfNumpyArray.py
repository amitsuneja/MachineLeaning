import numpy as np
"""
Create array of this way:
[[0 1 2 3]
 [1 2 3 4]
 [2 3 4 5]
 [3 4 5 6]
 [4 5 6 7]
 [5 6 7 8]
 [6 7 8 9]]
"""


def rolling(a_array, window):
    shape = (a_array.size - window + 1, window)
    strides = (a_array.itemsize, a_array.itemsize)
    return np.lib.stride_tricks.as_strided(a_array, shape=shape, strides=strides)


my_array = np.arange(10)
print(rolling(my_array, 4))