"""
File: fire.py
Name: Renee
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Highlight the fire areas in the given image.
    :param filename: The file path of the image to be processed.
    :return: The processed image with fire areas highlighted.
    """
    highlighted_fire = SimpleImage(filename)
    for pixel in highlighted_fire:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return highlighted_fire


def main():
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()

    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
