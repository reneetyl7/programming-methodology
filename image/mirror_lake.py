"""
File: mirror_lake.py
Name: Renee
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: The file path of the image to be processed.
    :return: The processed image with expand area.
    """
    img = SimpleImage(filename)
    expand_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            expand_img_p = expand_img.get_pixel(x, y)
            expand_img_p.red = img_p.red
            expand_img_p.green = img_p.green
            expand_img_p.blue = img_p.blue
            # flip and add on the expand area
            expand_img_p2 = expand_img.get_pixel(x, expand_img.height-1-y)
            expand_img_p2.red = expand_img_p.red
            expand_img_p2.green = expand_img_p.green
            expand_img_p2.blue = expand_img_p.blue
    return expand_img


def main():
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
