"""
argmin and argmax:
By adding the axis argument, NumPy looks at the rows and columns individually.
When it's not given, the array a is flattened into a single 1D array.

axis=0 means that the operation is performed down the columns of a 2D array a in turn.
For example np.argmin(a, axis=0) returns the index of the minimum value in each of the four columns.


axis=1 means that the operation is performed across the rows of a.
That means np.argmin(a, axis=1) returns [0, 2, 2] because a has three rows.
The index of the minimum value in the first row is 0,
the index of the minimum value of the second and third rows is 2.
"""




import numpy as np
a = np.array([[1, 2, 4, 7], [9, 88, 6, 45], [9, 76, 3, 4]])

print(a)
"""
[[ 1  2  4  7]
 [ 9 88  6 45]
 [ 9 76  3  4]]
"""


print(a.shape)
"""
(3, 4)
"""


print(a.size)
"""
12
"""



print(np.argmax(a))
"""
5
"""



print(np.argmax(a, axis=0))
"""
[1 1 1 1]
"""



print(np.argmax(a, axis=1))
"""
[3 1 1]
"""



print(np.argmin(a))
"""
0
"""



print(np.argmin(a, axis=0))
"""
[0 0 2 2]
"""



print(np.argmin(a, axis=1))
"""
[0 2 2]
"""