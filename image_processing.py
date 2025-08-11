from PIL import Image
import numpy as np

def find_closest_color(pixel, palette):
    """Find the closest color in the palette to the given pixel using Euclidean distance."""
    pixel = np.array(pixel)
    palette = np.array(palette)
    distances = np.sqrt(((palette - pixel) ** 2).sum(axis=1))
    return (palette[np.argmin(distances)])

def pixelate_and_quantize_image(input_path, output_path, palette=None):

    
    # Load the image
    image = Image.open(input_path).convert("RGB")
    
    # Pixelate: Resize down and back up

    # pixelated = image.resize(image.size, Image.Resampling.NEAREST)
    
    # Convert to numpy array for processing
    img_array = np.array(image)
    print(img_array)
    # Quantize colors to the palette
    height, width, _ = img_array.shape
    running = True
    for y in range(height):
        for x in range(width):
            color = find_closest_color(img_array[y, x], palette)
            print(y, x)
            color  = (tuple(color.tolist()))
            print(color)
            print(palette[1])

            # input()
            #yellow to orange
            #green to yellow

            #
            #yellow to green
            #green to orange
            if tuple(color) == palette[1]:
                print("green to yellow")
                # input()
                img_array[y,x] = palette[4]
            elif tuple(color) == palette[4]:
                print("yellow to orange")
                img_array[y,x] = palette[2]
            else:
                print("error")
                break
            color = find_closest_color(img_array[y, x], palette)
            color = tuple(color.tolist())
            print(color)
            print(palette[2])
            print(color == palette[2])
            if color != palette[2] and color != palette[4]:
                print("Error")
                running = False
                break 
        if not running:
            break
            # img_array[y, x] = find_closest_color(img_array[y, x], palette)
    
    # Convert back to image and save
    print(img_array)
    quantized_image = Image.fromarray(img_array)
    quantized_image.save(output_path)

# Example usage
input_image = "Left.png"  # Replace with your JPEG file path
output_image = "pixelated_quantized_output.jpg"
custom_palette = [(255, 255, 255), (0, 255, 0), (255, 153, 0), (0, 0, 255), (255,255,0), (255, 0 ,0)]  # Example palette
pixelate_and_quantize_image(input_image, output_image, palette=custom_palette)