import numpy as np
from matplotlib import pyplot as plt


data = np.array([
    [1, 2],
    [2, 3],
    [3, 6],
])
x, y = data.T
plt.plot(x, y, 'ro-')
plt . show()
