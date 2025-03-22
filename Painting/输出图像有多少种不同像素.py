import numpy as np
from PIL import Image

def count_unique_pixels(image_path):
    # Load the image
    image = Image.open(image_path)
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Get the unique pixel values
    unique_pixels, counts = np.unique(image_array, return_counts=True)
    # Return the number of unique pixels
    return unique_pixels, counts

# Example usage
image_path = r'C:\Yan3\Algorithm-version2\Painting\DukeDME\new_label.png'
unique_pixels, counts = count_unique_pixels(image_path)
for pixel, count in zip(unique_pixels, counts):
    print(f"Pixel value: {pixel}, Count: {count}")

