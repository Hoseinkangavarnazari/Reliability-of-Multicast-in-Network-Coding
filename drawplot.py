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
    [3, 368.8/8],
    [5, 285.42/8],
    [10,201.85/8],
    [17,154.79/8],
    [25, 127.64/8],
    [35, 107.88/8],
    [50, 90.26/8]

])
x, y = data.T
plt.plot(x, y, 'ro-')
plt . show()


def makePlot():
    return True
