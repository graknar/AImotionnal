import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_4D_dataframe(data):
    # Assumons que les dimensions de 'data' sont (x, y, z, color)
    x_dim, y_dim, z_dim, color_dim = data.shape
    
     # Extraire les données pour la coupe spécifiée
    X, Y = np.meshgrid(np.arange(x_dim), np.arange(y_dim))
    Z = np.mean(data, axis=3).mean(axis=0)  # Utilise la moyenne ou une autre opération pour obtenir Z
    
    # Crée une figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crée le plot de surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    
    # Ajoute une barre de couleur pour la quatrième dimension
    fig.colorbar(surf, ax=ax, label='Fourth Dimension Value')
    
    # Définit les labels des axes
    ax.set_xlabel('X Dimension')
    ax.set_ylabel('Y Dimension')
    ax.set_zlabel('Z Dimension')
    
    # Affiche le plot
    plt.title(f'Combined Surface')
    plt.show()