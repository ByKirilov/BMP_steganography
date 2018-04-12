import unittest
import Helper as H


class TestHelper(unittest.TestCase):
    def test_bytes_to_int(self):
        self.assertEqual(0, H.bytes_to_int(b'\x00'))
        self.assertEqual(16, H.bytes_to_int(b'\x10'))
        self.assertEqual(16, H.bytes_to_int(b'\x10\x00'))
        self.assertEqual(4096, H.bytes_to_int(b'\x00\x10'))

    def test_get_bits(self):
        self.assertEqual('00000000', H.get_bits(0))
        self.assertEqual('00000011', H.get_bits(3))
        self.assertEqual('11111111', H.get_bits(255))
        self.assertRaises(ValueError, H.get_bits, 500)
        self.assertRaises(ValueError, H.get_bits, -5)


if __name__ == '__main__':
    unittest.main()
