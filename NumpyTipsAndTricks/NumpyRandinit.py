import numpy as np

# Generate A Random Number From The Normal Distribution
print(np.random.normal())

# Generate Four Random Numbers From The Normal Distribution
print(np.random.normal(size=4))

# Generate Four Random Numbers From The Uniform Distribution
print(np.random.uniform(size=4))

# Generate Four Random Integers Between 1 and 100
print(np.random.randint(low=1, high=100, size=4))
print(np.random.randint(1, 100, size=4))

x = np.random.randint(16, size=(4, 4)).astype('uint8')
print(x)

print(np.random.randint(2, size=10))
print(np.random.randint(1, size=10))