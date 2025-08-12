import numpy as np

# Fixed color mapping
color_map = {
    (255, 255, 255): 1,  # White
    (0, 255, 0): 2,      # Green
    (255, 153, 0): 3,    # Orange
    (255, 0, 0): 4,      # Red
    (0, 0, 255): 5,      # Blue
    (255, 255, 0): 6     # Yellow
}

# Convert dict to arrays for vectorized math
palette_colors = np.array(list(color_map.keys()))
palette_values = np.array(list(color_map.values()))

def nearest_color(pixel, i=1):
    """
    Returns the i-th nearest color number to the given pixel.
    
    pixel: tuple or list or numpy array (R, G, B)
    i: rank of nearest color (1 = nearest, 2 = second nearest, etc.)
    """
    pixel = np.array(pixel)
    distances = np.sqrt(np.sum((palette_colors - pixel) ** 2, axis=1))
    
    sorted_indices = np.argsort(distances)
    
    if 1 <= i <= len(palette_colors):
        return palette_values[sorted_indices[i-1]]
    else:
        raise ValueError(f"i must be between 1 and {len(palette_colors)}")

# Example usage
print(nearest_color((250, 250, 250), i=1))  # Nearest to white
print(nearest_color((250, 250, 250), i=2))  # Second nearest
print(nearest_color((100, 200, 50), i=3))   # Third nearest
