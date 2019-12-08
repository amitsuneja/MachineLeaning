import numpy as np

array1 = np.arange(21, 30)
array2 = np.arange(11, 20)
array3 = np.ones(9)

print(array1)
print(array2)
print(array3)
print(array1.shape)
print(array2.shape)
print(array3.shape)
"""
[21 22 23 24 25 26 27 28 29]
[11 12 13 14 15 16 17 18 19]
[1. 1. 1. 1. 1. 1. 1. 1. 1.]
(9,)
(9,)
(9,)
"""

my_matrix = np.c_[array3, array2, array1]
print(my_matrix)
print(my_matrix.shape)

"""
[[ 1. 11. 21.]
 [ 1. 12. 22.]
 [ 1. 13. 23.]
 [ 1. 14. 24.]
 [ 1. 15. 25.]
 [ 1. 16. 26.]
 [ 1. 17. 27.]
 [ 1. 18. 28.]
 [ 1. 19. 29.]]
(9, 3)
"""

my_matrix = np.stack([array3, array2, array1], axis=1)
print(my_matrix)
print(my_matrix.shape)
"""
[[ 1. 11. 21.]
 [ 1. 12. 22.]
 [ 1. 13. 23.]
 [ 1. 14. 24.]
 [ 1. 15. 25.]
 [ 1. 16. 26.]
 [ 1. 17. 27.]
 [ 1. 18. 28.]
 [ 1. 19. 29.]]
(9, 3)
"""