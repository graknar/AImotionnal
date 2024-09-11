import numpy as np
import matplotlib.pyplot as plt

def plot_4d_dataframe(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(data.shape[0])
    y = np.arange(data.shape[1])
    z = np.arange(data.shape[2])
    c = data.flatten()

    x, y, z = np.meshgrid(x, y, z)
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    # Ajuster la taille de c pour qu'elle corresponde à x et y
    if len(c) != len(x):
        c = c[:len(x)]

    ax.scatter(x, y, z, c=c, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()