"""
The numpy.squeeze() function removes single-dimensional entries from the shape of an array
numpy.squeeze(a, axis=None)


"""


import numpy as np

my_array = np.array([[[12, 42, 22], [9, 12, 2]]])
print("my_array=", my_array)
print("my_array.shape=", my_array.shape)  # (1, 2, 3)
"""
Notice array shape changed from (1, 2, 3) to (2, 3)
"""
squeeze_array = np.squeeze(my_array)
print("squeeze_array=", squeeze_array)
print("squeeze_array.shape=", squeeze_array.shape)  # (2, 3)
"""
Notice cant squeeze (2, 3) further means result is (2,3) same as input.
"""
squeeze_array = np.squeeze(squeeze_array)
print("squeeze_array=", squeeze_array)
print("squeeze_array.shape=", squeeze_array.shape)  # (2, 3)

