import numpy as np
# Make numpy print 4 significant digits for prettiness
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
import matplotlib
# Default to nearest neighbor interpolation, gray colormap
matplotlib.rcParams['image.interpolation'] = 'nearest'
matplotlib.rcParams['image.cmap'] = 'gray'


X = np.arange(25).reshape(5,5)
print(X)
imgplot = plt.imshow(X)
plt.show()
print(np.linalg.matrix_rank(X))