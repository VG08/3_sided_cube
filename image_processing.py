from PIL import Image
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

# ANSI escape code mapping for printing
ansi_map = {
    1: "\033[38;2;255;255;255m",  # White
    2: "\033[38;2;0;255;0m",      # Green
    3: "\033[38;2;255;153;0m",    # Orange
    4: "\033[38;2;255;0;0m",      # Red
    5: "\033[38;2;0;0;255m",      # Blue
    6: "\033[38;2;255;255;0m"     # Yellow
}
reset_color = "\033[0m"

# Convert dict to numpy array for fast distance computation
palette_colors = np.array(list(color_map.keys()))
palette_values = np.array(list(color_map.values()))

def nearest_color(pixel):
    """Return the number of the nearest color from the palette."""
    distances = np.sqrt(np.sum((palette_colors - pixel) ** 2, axis=1))
    return palette_values[np.argmin(distances)]

def image_to_color_array(image_path):
    # Open image and ensure RGB mode
    img = Image.open(image_path).convert("RGB")
    img = img.resize((30, 30))  # Ensure 30x30 size
    
    pixels = np.array(img)  # Shape: (30, 30, 3)

    # Vectorized mapping
    height, width, _ = pixels.shape
    result = np.zeros((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            result[i, j] = nearest_color(pixels[i, j])
    print_colored_array(array=result)
    return result

def print_colored_array(array):
    for row in array:
        for val in row:
            print(f"{ansi_map[val]}{val}{reset_color}", end=" ")
        print()

if __name__ == "__main__":
    path = "logo.png"  # Change this to your file path
    color_array = image_to_color_array(path)
    print_colored_array(color_array)
