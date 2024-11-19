"""
File: extension_blur.py
Name: Renee
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
(abbr. version)
"""
from simpleimage import SimpleImage


def blur(img):
    """
    Blurs the given image by taking the average RGB values of a pixel's nearest neighbors.
    Args: img (SimpleImage): The input image to be blurred.
    Returns: SimpleImage: The blurred image.
    """
    new_width = img.width
    new_height = img.height
    new_img = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            # Initialize the sum of RGB values
            total_red = 0
            total_green = 0
            total_blue = 0
            num_neighbors = 0

            # Iterate through the 3x3 neighborhood of the current pixel
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x = x + dx
                    new_y = y + dy

                    # Check if the neighbor pixel is within the image bounds
                    if 0 <= new_x < new_width and 0 <= new_y < new_height:
                        neighbor = img.get_pixel(new_x, new_y)
                        total_red += neighbor.red
                        total_green += neighbor.green
                        total_blue += neighbor.blue
                        num_neighbors += 1

            # Calculate the average RGB values and set the new pixel
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = total_red // num_neighbors
            new_pixel.green = total_green // num_neighbors
            new_pixel.blue = total_blue // num_neighbors

    return new_img


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()