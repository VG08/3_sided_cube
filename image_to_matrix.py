import numpy as np
from PIL import Image
import os

def get_cube_colors(image_path):
    """
    Analyzes an image of a 3x3 Rubik's cube side and returns a 3x3 array
    of color numbers.

    Args:
        image_path (str): The path to the image file.

    Returns:
        np.ndarray: A 3x3 NumPy array representing the colors on the cube side.
                    Returns None if the image file is not found.
    """
    # Define the color-to-number mapping and palette as per the spec
    color_map = {
        (255, 255, 255): 1,   # White
        (0, 255, 0): 2,       # Green
        (255, 153, 0): 3,     # Orange
        (255, 0, 0): 4,       # Red
        (0, 0, 255): 5,       # Blue
        (255, 255, 0): 6,     # Yellow
    }

    custom_palette = [
        (255, 255, 255),  # White
        (255, 255, 0),    # Yellow
        (255, 0, 0),      # Red
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (255, 153, 0),    # Orange
    ]

    if not os.path.exists(image_path):
        print(f"Error: The image file at '{image_path}' was not found.")
        return None

    try:
        # Open the image using Pillow and convert to RGB
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            # Convert the image to a NumPy array for easier processing
            img_array = np.array(img)

        # Get image dimensions
        height, width, _ = img_array.shape

        # Assume the cube takes up the entire image and is divided into 3x3 grid
        # Calculate the size of each sticker based on the image dimensions
        sticker_height = height // 3
        sticker_width = width // 3

        # Initialize an empty 3x3 array to store the color numbers
        cube_colors = np.zeros((3, 3), dtype=int)

        # Iterate through the 3x3 grid of stickers
        for row in range(3):
            for col in range(3):
                # Define the boundaries for the current sticker
                start_h = row * sticker_height
                end_h = start_h + sticker_height
                start_w = col * sticker_width
                end_w = start_w + sticker_width

                # Extract the sticker's pixel data from the image array
                sticker_pixels = img_array[start_h:end_h, start_w:end_w]

                # Calculate the average color of the sticker
                avg_color = np.mean(sticker_pixels, axis=(0, 1)).astype(int)

                # Find the closest color in the predefined palette using Euclidean distance
                closest_color_tuple = find_closest_color(avg_color, custom_palette)

                # Map the closest color tuple to its corresponding number
                if closest_color_tuple in color_map:
                    cube_colors[row, col] = color_map[closest_color_tuple]
                else:
                    # This case should not be reached if the palette is comprehensive
                    print(f"Warning: No matching color found for average color {avg_color}. Setting to 0.")
                    cube_colors[row, col] = 0

        return cube_colors

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def find_closest_color(rgb_color, palette):
    """
    Finds the closest color in a given palette to a target RGB color.
    Uses Euclidean distance for comparison.

    Args:
        rgb_color (np.ndarray): The target RGB color as a NumPy array.
        palette (list): A list of RGB color tuples.

    Returns:
        tuple: The RGB tuple from the palette that is closest to the target color.
    """
    distances = [
        np.sqrt(np.sum((np.array(rgb_color) - np.array(p)) ** 2))
        for p in palette
    ]
    closest_index = np.argmin(distances)
    return palette[closest_index]

def rotate_cube_side(cube_array, rotations=1):
    """
    Rotates a 3x3 NumPy array representing a cube side clockwise by 90 degrees.

    Args:
        cube_array (np.ndarray): The 3x3 NumPy array to rotate.
        rotations (int): The number of 90-degree clockwise rotations to perform.
                         A positive value rotates clockwise, a negative value rotates counter-clockwise.

    Returns:
        np.ndarray: The rotated 3x3 NumPy array.
    """
    # Use np.rot90 with a negative k to rotate clockwise.
    # k=-1 is 90 degrees clockwise, k=-2 is 180 degrees, etc.
    return np.rot90(cube_array, k=-rotations)


# --- Main execution block ---
def convert_to_matrix(image_file):
    # IMPORTANT: Replace 'cube_side.png' with the actual path to your image file.
    # The program assumes a square image with a clear 3x3 grid.

    print(f"Analyzing image: {image_file}")
    color_array = get_cube_colors(image_file)

    if color_array is not None:

        # Demonstrate the new rotation function
        rotated_array = rotate_cube_side(color_array)
        print(color_array)
        # print(rotated_array)
        return color_array


# if __name__ == "__main__":
#     convert_to_matrix("right.jpg")