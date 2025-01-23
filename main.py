import random
import time
import numpy as np

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

num_segments = 100000  
region = [-1, -1, 3, 2] # interest as [x_min, y_min, x_max, y_max]


segments = generate_segments(num_segments)


start_time_numpy = time.time()
filtered_segments_numpy = filter_segments_numpy(segments, region)
end_time_numpy = time.time()


print(f"Number of segments before filtering: {len(segments)}")
print(f"Number of segments after numpy filtering: {len(filtered_segments_numpy)}")
print(f"Time taken with numpy: {end_time_numpy - start_time_numpy:.4f} seconds")
