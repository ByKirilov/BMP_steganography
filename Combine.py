import sys

from MyBMPImage import MyBMPImage
from MyFile import MyFile


def try_open_image(image_path, bits_to_rewrite_count):
    """
    Preparation of the object image
    :param image_path:
    :param bits_to_rewrite_count:
    """
    img = MyBMPImage(image_path, bits_to_rewrite_count)
    return img


def try_open_file(file_path, key):
    """
    Preparation of the object file
    :param file_path:
    :param key:
    """
    file = MyFile(file_path, key)
    return file


def combine(image_path, text_path, key, bits_to_rewrite_count):
    """
    Hides the text in the picture
    :param image_path:
    :param text_path:
    :param key:
    :param bits_to_rewrite_count:
    """
    image = try_open_image(image_path, bits_to_rewrite_count)
    file = try_open_file(text_path, key)

    if file.Finally_size > image.Volume:
        sys.exit("File too large!")

    image.new_image(file.Binary_string)


if __name__ == '__main__':
    print()
    print('Input image path:')
    image_path = input()
    print()
    print('Input text file path:')
    text_path = input()
    print()
    print('Input number of rewritable minor bits:')
    bits_to_rewrite_count = int(input())
    print()
    print('Input encryption key:')
    key = input()
    print()
    combine(image_path, text_path, key, bits_to_rewrite_count)
    print('OK')
