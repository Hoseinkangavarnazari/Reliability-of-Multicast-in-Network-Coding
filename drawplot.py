import numpy as np
from matplotlib import pyplot as plt
    # [0,  18.84],
    # [5, 6.718],
    # [10, 2.122],
    # [15, 0.8468],
    # [17,0.925],
    # [25, 0.464],
    # [35, 0.17726],
    # [50, 0.1562],
    # [60, 0]


data = np.array([
    [0,  19.58],
    [3, 8.28],
    [5, 6.74],
    [10, 2.92],
    [17,0.951],
    [25, 0.467],
    [35, 0.181334],
    [50, 0.16],
    [60, 0]

])
x, y = data.T
plt.plot(x, y, 'ro-')
plt . show()


def makePlot():
    return True
