import matplotlib.pyplot as plt
import numpy as np

def generate_heatmap(threat_data):
    board = np.array(threat_data).reshape(8, 8)  # 8x8 chess board
    plt.imshow(board, cmap='hot', interpolation='nearest')
    plt.title("Threat Heatmap")
    plt.colorbar(label="Threat Level")
    plt.show()

# Example: Random threat data for visualization
random_threat_data = np.random.randint(0, 10, 64)
generate_heatmap(random_threat_data)
