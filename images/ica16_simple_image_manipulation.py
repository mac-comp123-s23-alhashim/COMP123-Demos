from imageTools import *
from enum import Enum

class ColorType(Enum):
    GRAYSCALE = 1
    NEGATIVE = 2
    SHIFT_RIGHT = 3
    SHIFT_LEFT = 4
    RED_ONLY = 5
    GREEN_ONLY = 6
    BLUE_ONLY = 7
    REMOVE_BLUE = 8
    BLACK_WHITE = 9


def color_pixel(pixel: ImageColor, color_type: ColorType) -> ImageColor:
    (r, g, b) = pixel
    new_pixel = r, g, b

    if color_type == ColorType.GRAYSCALE:
        new_color = (r + g + b) / 3
        new_pixel = new_color, new_color, new_color
    elif color_type == ColorType.NEGATIVE:
        new_pixel = 255 - r, 255 - g, 255 - b
    elif color_type == ColorType.SHIFT_RIGHT:
        new_pixel = b, r, g
    elif color_type == ColorType.SHIFT_LEFT:
        new_pixel = g, b, r
    elif color_type == ColorType.RED_ONLY:
        new_pixel = r, 0, 0
    elif color_type == ColorType.GREEN_ONLY:
        new_pixel = 0, g, 0
    elif color_type == ColorType.BLUE_ONLY:
        new_pixel = 0, 0, b
    elif color_type == ColorType.REMOVE_BLUE:
        new_pixel = r, b, 0
    elif color_type == color_type.BLACK_WHITE:
        if distance((r, b, b), "black") > distance((r, b, b), "white"):
            new_pixel = "black"
        else:
            new_pixel = "white"

    return new_pixel


def color_img(pic: Picture,
              color_type: ColorType,
              animate_every=None) -> Picture:
    new_pic = Picture(pic.getWidth(), pic.getHeight())
    for (x, y) in pic:
        new_pic.setColor(x, y, color_pixel(pic.getColor(x, y), color_type))
        if animate_every is not None:
            if (x + y) % animate_every == 0:
                new_pic.show()
    return new_pic


if __name__ == "__main__":
    pic = Picture("../data/SampleImages/astilbe.jpg")
    pic.show()

    previous_new_pic = None
    ColorType_Sample = [ColorType.BLACK_WHITE]
    for color_type in ColorType_Sample:
        print("Next Color: {}".format(color_type.name))
        input("Press enter to color...")
        new_pic = color_img(pic, color_type)
        if previous_new_pic is not None:
            previous_new_pic.hide()
        new_pic.show()
        previous_new_pic = new_pic

    input("Enter any key to exit")
