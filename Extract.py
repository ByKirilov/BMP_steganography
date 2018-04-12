import sys
import Helper as H

from MyBMPImage import MyBMPImage
from AESCipher import AESCipher
from io import StringIO
from io import BytesIO
import math
import os.path
import hashlib


def try_open_image(image_path, bits_to_rewrite_count):
    img = MyBMPImage(image_path, bits_to_rewrite_count)
    return img


def get_data(image_data, bits_to_rewrite_count, key):
    cipher = AESCipher(key)

    image_bytes_count = int(math.ceil(64 * 8 / bits_to_rewrite_count))

    i_str = StringIO()
    for i in range(image_bytes_count):
        i_str.write(H.get_bits(image_data[i])[-bits_to_rewrite_count:])
    bin_enc_size = i_str.getvalue()[:64*8]

    i_bytes = BytesIO()
    for i in range(64):
        i_bytes.write(bytes([int(bin_enc_size[8 * i:8 * i + 8], 2)]))
    enc_size = i_bytes.getvalue()

    size = int(cipher.decrypt(enc_size))

    shift = image_bytes_count

    image_bytes_count = int(math.ceil(size * 8 / bits_to_rewrite_count))

    for i in range(image_bytes_count):
        i_str.write(H.get_bits(image_data[i+shift])[-bits_to_rewrite_count:])
    bin_enc_data = i_str.getvalue()[64*8:(size+64)*8]

    i_bytes = BytesIO()
    for i in range(size):
        i_bytes.write(bytes([int(bin_enc_data[8*i:8*i+8], 2)]))
    enc_data = i_bytes.getvalue()

    data = cipher.decrypt(enc_data).encode()
    return data


def extract(image_path, key, bits_to_rewrite_count):
    image = try_open_image(image_path, bits_to_rewrite_count)

    try:
        data = get_data(image.Image_Data, bits_to_rewrite_count, key)
    except:
        sys.exit('Wrong image or entered data')

    hash_sum = data[:32].decode()
    name_len = data[32]
    name = data[33:33+name_len]
    file_bytes = data[33+name_len:]

    if not hash_sum == hashlib.md5(file_bytes).hexdigest():
        sys.exit("Hash sums don't match")

    dir_file_path = os.path.dirname(image_path)
    # file_path = dir_file_path + '/' + name.decode()
    file_path = os.path.join(dir_file_path, name.decode())

    file = open(file_path, 'wb')
    file.write(file_bytes)
    file.close()


if __name__ == '__main__':
    print()
    print('Input image path:')
    image_path = input()
    print()
    print('Input number of rewritable minor bits:')
    bits_to_rewrite_count = int(input())
    print()
    print('Input encryption key:')
    key = input()
    print()
    extract(image_path, key, bits_to_rewrite_count)
    print('OK')
