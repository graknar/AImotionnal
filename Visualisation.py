import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata

def plot_4D_dataframe(data):
    # Assumons que les dimensions de 'data' sont (x, y, z, color)
    x_dim, y_dim, z_dim, color_dim = data.shape
        
    # Crée une grille de points pour les dimensions x, y
    X, Y = np.meshgrid(np.arange(x_dim), np.arange(y_dim))
    Z = np.mean(data, axis=3).mean(axis=0)  # Utilise la moyenne ou une autre opération pour obtenir Z
    
    # Création d'une grille plus dense pour l'interpolation
    X_dense, Y_dense = np.linspace(0, x_dim-1, 100), np.linspace(0, y_dim-1, 100)
    X_dense, Y_dense = np.meshgrid(X_dense, Y_dense)
    
    # Interpolation des données
    Z_dense = griddata((X.flatten(), Y.flatten()), Z.flatten(), (X_dense, Y_dense), method='cubic')
    
    # Crée une figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crée le plot de surface lissée
    surf = ax.plot_surface(X_dense, Y_dense, Z_dense, cmap='viridis', edgecolor='none')
    
    # Ajoute une barre de couleur pour les valeurs combinées
    fig.colorbar(surf, ax=ax, label='Combined Value')
    
    # Définit les labels des axes
    ax.set_xlabel('X Dimension')
    ax.set_ylabel('Y Dimension')
    ax.set_zlabel('Z Dimension')
    
    # Affiche le plot
    plt.title(f'Smoothed Surface ')
    return fig