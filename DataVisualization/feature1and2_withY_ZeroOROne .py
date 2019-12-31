import numpy as np
import matplotlib.pyplot as plt

X1 = np.random.randn(100).reshape(100, 1)
X2 = np.random.randn(100).reshape(100, 1) * 5
Y = np.random.randint(2, size=100).reshape(100, 1)  # Generate 100 numbers between 0 and 1


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4), sharey=False, dpi=120)
ax1.scatter(X1, X2)
ax1.set_title("Can you compare 0 and 1?")
ax1.set_xlabel("X1")
ax1.set_ylabel("X2")
ax2.scatter(X1, X2, c=Y, s=40)
ax2.set_title("Can you compare 0 and 1?")
ax2.set_xlabel("X1")
ax2.set_ylabel("X2")
ax3.scatter(X1, X2, c=Y, s=40,  cmap=plt.cm.Spectral)
ax3.set_title("cmap=plt.cm.Spectral ")
ax3.set_xlabel("X1")
ax3.set_ylabel("X2")
plt.show()
