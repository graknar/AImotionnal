import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from Function.Visualisation import plot_4D_dataframe

# Fonction pour générer des données aléatoires
def generate_data():
    return np.random.normal(-1, 1, size=(10, 10, 10, 10))

def random_alteration(data):
    return data + np.random.normal(-1,1, size=data.shape)

# Configuration de Streamlit
st.title('Affichage de plot en direct via un stream')
placeholder = st.empty()

df = generate_data()

# Boucle pour mettre à jour les données et le graphique en temps réel
while True:
    df=random_alteration(df)
    fig = plot_4D_dataframe(df)
    placeholder.pyplot(fig)
    time.sleep(1)
    plt.close()