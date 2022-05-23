import numpy as np
from PIL import Image
import os

character_list = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`' + "'. "
character_list = character_list[::-1]

MAX_SCALE = (200, 60)


def scale_img(img: Image.Image):
    while True:
        scale = img.size
        if scale[0] > MAX_SCALE[0]:
            img = img.resize((int(scale[0] // 1.2), scale[1]), Image.ANTIALIAS)
        elif scale[1] > MAX_SCALE[1]:
            img = img.resize((int(scale[0]), int(scale[1] // 1.2)), Image.ANTIALIAS)
        else:
            return img


def find_image():
    for i in os.listdir(os.getcwd() + "\Image"):
        if i.endswith('.jpg') or i.endswith('.png') or i.endswith(".PNG"):
            print(i)
            return os.getcwd() + fr"\Image\{i}"


image = Image.open(find_image())
image = scale_img(image)


def image_to_array():
    return np.array(image.getdata())


def get_pixel_avg(pixels : list):
    total = 0
    for i in pixels:
        total += int(i)
    return total/3


def avg_pixels_to_array():
    array = []
    image_array = image_to_array()
    for i in image_array:
        array.append(get_pixel_avg(i))
    return array


def avg_to_ascii(pixels : list):
    array = []
    list_len = len(character_list)
    for i in pixels:
        for a in range(list_len):
            if i <= (255/list_len) * (a+1):
                array.append(character_list[a])
                break
    return array


def main():
    avg_pixels = avg_pixels_to_array()
    ascii_text = avg_to_ascii(avg_pixels)

    readable = ""
    doodoo = ""
    for i in range(len(ascii_text)):
        if i % image.size[0] == 0:
            readable += '\n'
        readable += str(ascii_text[i])

    with open('output.txt', 'w') as f:
        f.write(readable)
    print("\nASCII image:" + readable)
    input()


if __name__ == '__main__':
    main()
