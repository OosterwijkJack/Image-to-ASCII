import numpy as np
from PIL import Image
import os

character_list = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`' + "'. "
character_list = character_list[::-1]

SCALE = (200, 60)


#  Picks up jpg and png image
def find_image():
    for i in os.listdir(os.getcwd() + "\Image"):
        if i.endswith('.jpg') or i.endswith('.png') or i.endswith(".PNG"):
            print(i)
            return os.getcwd() + fr"\Image\{i}"


image = Image.open(find_image())
image = image.resize((SCALE[0], SCALE[1]), Image.ANTIALIAS)


#  Pixel average is used to find brightness of pixel
def get_pixel_avg(pixels : list):
    total = 0
    for i in pixels:
        total += int(i)
    return total/3


#  places avg pixel data into array for each pixel
def avg_pixels_to_array():
    array = []
    image_array = np.array(image.getdata())
    for i in image_array:
        array.append(get_pixel_avg(i))
    return array


#  loops through average pixel array and assigns ascii text according to pixel brightness
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

    #  Loops through ascii list and displays to console while moving to next line depending on original images x
    readable = ""
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
