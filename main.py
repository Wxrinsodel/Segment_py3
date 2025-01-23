import random
import time

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

region = [-1, -1, 3, 2]

def filter_segments(segments, region):
    filtered_segments = []
    x_min, y_min, x_max, y_max = region
    
    for seg in segments:
        x1, y1, x2, y2 = seg
        if (x_min <= x1 <= x_max and y_min <= y1 <= y_max and
            x_min <= x2 <= x_max and y_min <= y2 <= y_max):
            filtered_segments.append(seg)
    
    return filtered_segments

segments = generate_segments(100000)

start_time = time.time()
filtered_segments = filter_segments(segments, region)
end_time = time.time()

print(f"Number of segments before filtering: {len(segments)}")
print(f"Number of segments after filtering: {len(filtered_segments)}")
print(f"Time taken without numpy: {end_time - start_time:.4f} seconds")
