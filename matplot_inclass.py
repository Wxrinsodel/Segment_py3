import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points.csv', delimiter=',')
distances = np.loadtxt('distances.csv')

plt.figure(figsize=(10, 8))
scatter = plt.scatter(points[:, 0], points[:, 1], 
                      c=distances, 
                      cmap='viridis', #perceptually uniform colormap that transitions smoothly
                      s=50,  
                      alpha=0.7)  # transparency

plt.colorbar(scatter, label='Distance')
plt.title('Scatter Plot of Points Colored by Distances')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
