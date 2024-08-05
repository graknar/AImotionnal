import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def plot_4d_dataframe(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(data.shape[0])
    y = np.arange(data.shape[1])
    z = np.arange(data.shape[2])
    c = np.arange(data.shape[3]).flatten()

    xs, ys, zs = [], [], []
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                xs.append((x[i] - min(x)) / (max(x) - min(x)) * 2 - 1)
                ys.append((y[j] - min(y)) / (max(y) - min(y)) * 2 - 1)
                zs.append((z[k] - min(z)) / (max(z) - min(z)) * 2 - 1)

    ax.scatter(xs, ys, zs, c=c, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
