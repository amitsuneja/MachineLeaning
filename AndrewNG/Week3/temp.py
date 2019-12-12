import numpy as np
import pickle

with open('pickle_file.pkl', "rb") as f:  # Python 3: open(..., 'rb')
    h, y, x = pickle.load(f)



y = y.to_numpy()
print(h.shape)
print(y.shape)
print(x.shape)
print(type(h))
print(type(y))
print(type(x))
print((h-y)*x)



