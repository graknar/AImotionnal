from Visualisation import plot_4d_dataframe
import numpy as np

def run():
    # Create a 4D array of random values
    data = np.random.uniform(-1, 1, size=(100, 100, 100, 100))

    # Call the plot_4d_dataframe function
    plot_4d_dataframe(data)

if __name__ == "__main__":
    run()