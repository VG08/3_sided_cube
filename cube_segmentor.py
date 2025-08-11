import os
from PIL import Image

def split_image_into_color_limited_cubes(image_path, output_dir, prefixes, num_colors):
    """
    Reduces the colors of an image, then divides it into 100 smaller
    3x3 pixel images with a specific naming convention.

    Args:
        image_path (str): The path to the input image.
        output_dir (str): The directory where the output images will be saved.
        prefixes (list): A list of characters for the output filenames.
        num_colors (int): The number of colors to reduce the image to.
    """
    try:
        # Open the input image
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
        return

    # For 100 faces, we need a 10x10 grid of 3x3 pixel cubes.
    # This requires a 30x30 pixel image.
    img_resized = img.resize((30, 30))

    # --- New Step: Color Quantization ---
    # Reduce the image to a specific number of colors.
    # The 'quantize()' method creates an adaptive palette. [3]
    # Note: quantize converts the image to 'P' (palette) mode. We convert
    # it back to 'RGB' to ensure the saved PNGs are in a standard color format.
    img_quantized = img_resized.quantize(colors=num_colors, method=Image.FASTOCTREE)
    img_final = img_quantized.convert('RGB')

    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    tile_size = 3
    num_tiles_per_row = 10
    prefix_index = 0
    file_counter = 1

    # Iterate through the 10x10 grid
    for row in range(num_tiles_per_row):
        for col in range(num_tiles_per_row):
            # Define the box for cropping
            left = col * tile_size
            upper = row * tile_size
            right = left + tile_size
            lower = upper + tile_size
            box = (left, upper, right, lower)

            # Crop the color-reduced image to get the 3x3 tile
            tile = img_final.crop(box)

            # Construct the output filename
            if prefix_index < len(prefixes):
                prefix = prefixes[prefix_index]
                filename = f"{prefix}{file_counter}.png"
                output_path = os.path.join(output_dir, filename)

                # Save the cropped tile
                tile.save(output_path)
                print(f"Saved {output_path}")

                file_counter += 1
            else:
                print("Warning: Ran out of prefixes for naming files.")
                break
        
        if prefix_index >= len(prefixes):
            break

        # Move to the next prefix for the next row of tiles
        prefix_index += 1
        file_counter = 1

if __name__ == '__main__':
    # --- Configuration ---
    # The path to your input image
    input_image_path = 'Right.png'
    
    # The directory where the smaller images will be saved
    output_folder = 'cube_faces_right'
    
    # The prefixes for the filenames (one for each of the 10 rows)
    naming_prefixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    # The total number of colors you want in the final set of images
    number_of_colors = 16

    # --- Run the main function ---
    split_image_into_color_limited_cubes(input_image_path, output_folder, naming_prefixes, number_of_colors)