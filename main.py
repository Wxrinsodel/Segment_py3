import random
import time
import numpy as np
import matplotlib.pyplot as plt

def generate_segments(num_segments):
    segments = []
    for _ in range(num_segments):
        x1 = random.uniform(-10, 10)
        y1 = random.uniform(-10, 10)
        x2 = random.uniform(-10, 10)
        y2 = random.uniform(-10, 10)
        segment = [x1, y1, x2, y2]
        segments.append(segment)
    return segments

def filter_segments_numpy(segments, region):
    x_min, y_min, x_max, y_max = region

    # Convert segments to numpy array for vectorized operations
    segments = np.array(segments) 

    x1, y1, x2, y2 = segments[:, 0], segments[:, 1], segments[:, 2], segments[:, 3]
    
    mask = (
        (x_min <= x1) & (x1 <= x_max) & 
        (y_min <= y1) & (y1 <= y_max) &
        (x_min <= x2) & (x2 <= x_max) &
        (y_min <= y2) & (y2 <= y_max)
    )
    
    filtered_segments = segments[mask]
    
    return filtered_segments.tolist()

num_segments = 1000
region = [-1, -1, 3, 2] # interest as [x_min, y_min, x_max, y_max]

# Generate random segments
segments = generate_segments(num_segments)

# Measure performance for numpy filtering
start_time_numpy = time.time()
filtered_segments_numpy = filter_segments_numpy(segments, region)
end_time_numpy = time.time()

print(f"Number of segments before filtering: {len(segments)}")
print(f"Number of segments after numpy filtering: {len(filtered_segments_numpy)}")
print(f"Time taken with numpy: {end_time_numpy - start_time_numpy:.4f} seconds")

# Visualization using matplotlib
def visualize_segments(segments, filtered_segments, region):
    plt.figure(figsize=(10, 8))
    
    # Plot all initial segments
    for seg in segments:
        x1, y1, x2, y2 = seg
        plt.plot([x1, x2], [y1, y2], color='gray', alpha=0.5, label='Initial Segments' if 'gray' not in plt.gca().lines else "")
    
    # Plot filtered segments
    for seg in filtered_segments:
        x1, y1, x2, y2 = seg
        plt.plot([x1, x2], [y1, y2], color='blue', linewidth=1.5, label='Filtered Segments' if 'blue' not in plt.gca().lines else "")
    
    # Plot the region of interest
    x_min, y_min, x_max, y_max = region
    plt.plot(
        [x_min, x_max, x_max, x_min, x_min], 
        [y_min, y_min, y_max, y_max, y_min], 
        color='red', linestyle='--', label='Region of Interest'
    )
    
    # Labels and legend
    plt.title("Segments Visualization", fontsize=16)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.legend(loc="upper right")
    plt.grid(alpha=0.3)
    plt.show()

# Call the visualization function
visualize_segments(segments, filtered_segments_numpy, region)
