import unittest
import Helper as H

from io import StringIO
from MyBMPImage import MyBMPImage

class TestMyBMPImage(unittest.TestCase):
    def test_new_image(self):
        img = MyBMPImage('/media/ars/Data/HW/Python/Task/Стеганография bmp/for_test/bmp-wb.bmp', 8)
        str_b = StringIO()
        for i in range(626*626):
            str_b.write(H.get_bits(int.from_bytes(b'\x08', byteorder='little')))
        str = str_b.getvalue()
        img.new_image(str)

if __name__ == '__main__':
    unittest.main()
