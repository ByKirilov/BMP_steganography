import Extract
import Combine
import shutil
import sys

print(int.from_bytes(b'a', byteorder='little'))
input()


img_path = '/media/ars/Data/HW/Python/Task/Стеганография bmp/for_test/bmp-cl-big.bmp'
text_path = '/media/ars/Data/HW/Python/Task/Стеганография bmp/for_test/1.txt'
# text_path = '/media/ars/Data/HW/Python/Task/Стеганография bmp/for_test/0'
bits_to_rewrite = 2
key = 'qwerty'
Combine.combine(img_path, text_path, key, bits_to_rewrite)

shutil.move('/media/ars/Data/HW/Python/Task/Стеганография bmp/for_test/Combined image.bmp',
            '/media/ars/Data/HW/Python/Task/Стеганография bmp/temp/')


comb_img_path = '/media/ars/Data/HW/Python/Task/Стеганография bmp/temp/Combined image.bmp'
Extract.extract(comb_img_path, key, bits_to_rewrite)