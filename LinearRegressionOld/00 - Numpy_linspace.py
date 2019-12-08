
# what is coefficient ?
# 6z means 6 times z, and "z" is a variable, so 6 is a coefficient

import numpy as np
import matplotlib.pyplot as plt


# np.linspace (start,stop,num=<int>,retstep=True)
# start  : [optional] start of interval range. By default start = 0
# stop   : end of interval range
# restep : If True, return (samples, step). By deflut restep = False
# num    : [int, optional] No. of samples to generate
# dtype  : type of output array

# re-step set to True
print("A (step of .025) =", np.linspace(2.0, 3.0, num=5, retstep=True))
print("B (step of .05)  =", np.linspace(2.0, 4.0, 5, retstep=True))
print("B (step of .05)  =", np.linspace(2.0, 4.0, 5, retstep=True, dtype=bytearray))
print("_____________________________________________________________")

# To evaluate sin() in long range
x = np.linspace(0, 2, 10)
print(x)
print(np.sin(x))

# Graphical Represenation of numpy.linspace()
# Start = 0
# End = 2
# Samples to generate = 10
x1 = np.linspace(0, 2, 10, endpoint=False)
y1 = np.ones(10)
print(x1, y1)
plt.plot(x1, y1, "*")
plt.xlim(-0.2, 1.8)
plt.show()


