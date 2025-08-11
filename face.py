import numpy as np
from PIL import Image
import os

class CubeFace:
    """
    Represents a single face of a Rubik's cube, handling image-to-matrix conversion.
    
    Attributes:
        image_path (str): The file path for the cube face image.
        matrix (np.ndarray): The 3x3 NumPy array representing the colors on the face.
    """
    # Static color definitions based on the provided specifications
    _COLOR_MAP = {
        (255, 255, 255): 1,   # White
        (0, 255, 0): 2,       # Green
        (255, 153, 0): 3,     # Orange
        (255, 0, 0): 4,       # Red
        (0, 0, 255): 5,       # Blue
        (255, 255, 0): 6,     # Yellow
    }
    _PALETTE = list(_COLOR_MAP.keys())

    def __init__(self, matrix):
        """
        Initializes a CubeFace by loading an image and generating its color matrix.

        Args:
            image_path (str): The path to the image file of the cube face.
        
        Raises:
            FileNotFoundError: If the image file cannot be found.

        # self.image_path = image_path
x        """
        self.matrix = matrix
    def _find_closest_color(self, rgb_color):
        """Finds the closest color in the predefined palette using Euclidean distance."""
        distances = [
            np.sqrt(np.sum((np.array(rgb_color) - np.array(p)) ** 2))
            for p in self._PALETTE
        ]
        closest_index = np.argmin(distances)
        return self._PALETTE[closest_index]

    def _generate_matrix_from_image(self):
        """Analyzes the image and returns a 3x3 array of color numbers."""
        try:
            with Image.open(self.image_path) as img:
                img = img.convert('RGB')
                img_array = np.array(img)

            height, width, _ = img_array.shape
            sticker_height, sticker_width = height // 3, width // 3
            cube_colors = np.zeros((3, 3), dtype=int)

            for row in range(3):
                for col in range(3):
                    sticker_pixels = img_array[
                        row * sticker_height : (row + 1) * sticker_height,
                        col * sticker_width : (col + 1) * sticker_width
                    ]
                    avg_color = np.mean(sticker_pixels, axis=(0, 1)).astype(int)
                    closest_color = self._find_closest_color(avg_color)
                    cube_colors[row, col] = self._COLOR_MAP[closest_color]
            
            return cube_colors
        except Exception as e:
            print(f"An error occurred while processing {self.image_path}: {e}")
            return np.zeros((3, 3), dtype=int)

    @property
    def center(self):
        """Returns the color code of the center piece."""
        return self.matrix[1]

    @property
    def edges(self):
        """Returns a list of the four edge piece color codes."""
        return [self.matrix[0, 1], self.matrix[1, 0], self.matrix[1, 2], self.matrix[2, 1]]

    @property
    def corners(self):
        """Returns a list of the four corner piece color codes."""
        return [self.matrix[0, 0], self.matrix[0, 2], self.matrix[2, 0], self.matrix[2, 2]]

    def __str__(self):
        """String representation of the face's matrix."""
        return str(self.matrix)