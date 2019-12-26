import numpy as np

"""
Assertions are statements that assert or state a fact confidently in your program. For example, while writing a division
function, you're confident the divisor shouldn't be zero, you assert divisor is not equal to zero.

Assertions are simply boolean expressions that checks if the conditions return true or not. 
If it is true, the program does nothing and move to the next line of code. However, if it's false, 
the program stops and throws an error.
"""
A = np.arange(5)
print(A.shape)   # (5,) Its rank 1 array and very bad for machine learning . Never use it .
assert(A.shape == (5, 1)),"you are not using correct shape of array , See console you can see this msg."



