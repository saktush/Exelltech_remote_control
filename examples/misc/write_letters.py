from PIL import Image
import numpy as np
from examples.misc.letters import LETTERS


def letter_to_binary(ch):
    return LETTERS.get(ch.upper(), [[0] * 5 for _ in range(7)])


def get_pixel_array(letters, width, height):
    binary_pixels = []

    # Create binary representation for letters and add a 1-pixel gap in between letters
    for letter in letters:
        binary_pixels.append(letter_to_binary(letter))
        binary_pixels.append([[0] * 1 for _ in range(7)])  # 1-pixel vertical gap

    # Remove the last gap
    if binary_pixels:
        binary_pixels.pop()

    # Combine all binary_pixels horizontally
    combined_pixels = np.hstack(binary_pixels)

    # Map 1 to (232, 23, 93) and 0 to (0, 0, 0)
    color_map = {1: (232, 23, 93), 0: (0, 0, 0)}
    pixels = [[color_map[pixel] for pixel in row] for row in combined_pixels]

    # Convert to numpy array
    pixel_array = np.array(pixels).astype(np.uint8)

    # Resize to the required dimensions
    pil_image = Image.fromarray(pixel_array)
    resized_image = pil_image.resize((width, height), Image.NEAREST)

    return np.array(resized_image)


def preview(letters="DIGIS"):
    # preview usage:
    width = 18
    height = 14
    pixels_array = get_pixel_array(letters, width, height)

    # Save image to visualize
    new_image = Image.fromarray(pixels_array)
    new_image.show("Preview")


if __name__ == '__main__':
    preview()
