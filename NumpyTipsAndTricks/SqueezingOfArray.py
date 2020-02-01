"""
The numpy.squeeze() function removes single-dimensional entries from the shape of an array
numpy.squeeze(a, axis=None)


"""
import numpy as np

w1 = np.array([1, 2]).reshape(1, 2)
w2 = np.array([3, 4]).reshape(1, 2)
w3 = np.array([5, 6]).reshape(1, 2)
w4 = np.array([7, 8]).reshape(1, 2)
W = np.stack((w1, w2, w3, w4))
print(W.shape)   # (4, 1, 2)
W = np.squeeze(W)
print(W.shape)  # (4, 2)
print(W)

