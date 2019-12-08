import matplotlib.pyplot as plt
import numpy as np

"""
Interpolation - means estimating value of "DataPoint" that lies between two  given data points.
Extrapolation - means estimation of a value based on extending a known sequence of values.
"""

a = np.arange(4)
p = np.linspace(0, 100, 300)
ax = plt.gca()
lines = [
    ('linear', None),
    ('higher', '--'),
    ('lower', '--'),
    ('nearest', '-.'),
    ('midpoint', '-.'),
]

for interpolation, style in lines:
    ax.plot(p, np.percentile(a, p, interpolation=interpolation),label=interpolation, linestyle=style)
ax.set(
    title='Interpolation methods for list: ' + str(a),
    xlabel='Percentile',
    ylabel='List item returned',
    yticks=a,
)
ax.legend()
plt.show()