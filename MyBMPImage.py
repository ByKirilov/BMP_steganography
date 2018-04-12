import os.path
import Helper as H
import sys


class MyBMPImage:
    # path, count of young rewrite symbols
    def __init__(self, path, bits_to_rewrite_count):
        self.Path = os.path.abspath(path)
        if not os.path.exists(self.Path):
            sys.exit('File does not exist!')
        if not os.path.isfile(self.Path):
            sys.exit(self.Path + ' - is not file!')

        try:
            image = open(path, 'rb')
        except Exception:
            sys.exit('Can not open file!')
        current_offset = 0

        self.Head = b''
        try:
            read = image.read(2)
            self.Type = read  # sygnatura
            self.Head += read
            current_offset += 2

            read = image.read(8)
            self.Head += read
            current_offset += 8

            read = image.read(4)
            offset_bits = H.bytes_to_int(read)  # shift to start of data
            self.Head += read
            current_offset += 4
        except Exception:
            sys.exit('Wrong BitMapFileHeader!')

        try:
            read = image.read(4)
            self.Head += read
            current_offset += 4

            read = image.read(4)
            self.Width = H.bytes_to_int(read)  # Width
            self.Head += read
            current_offset += 4

            read = image.read(4)
            self.Height = H.bytes_to_int(read)  # height
            self.Head += read
            current_offset += 4

            read = image.read(2)
            self.Head += read
            current_offset += 2

            read = image.read(2)
            self.Bit_count = H.bytes_to_int(read)  # color depth
            self.Head += read
            current_offset += 2

            read = image.read(4)
            self.Head += read
            current_offset += 4

            read = image.read(4)
            self.Size = H.bytes_to_int(read)  # image size
            self.Head += read
            current_offset += 4

            read = image.read(offset_bits - current_offset)
            self.Head += read
            current_offset += offset_bits - current_offset
        except Exception:
            sys.exit('Wrong BitMapInfoHeader!')

        try:
            self.Image_Data = image.read()
        except Exception:
            sys.exit('Wrong Image!')

        if self.Type != b'BM':
            sys.exit('Is not BMP image!')

        self.Bits_to_rewrite_count = bits_to_rewrite_count

        self.Volume = self.Size // (8 / bits_to_rewrite_count) * 3

        image.close()

    def rewrite(self, data):
        img = open(self.Path, 'wb')
        img.write(self.Head)
        shift = 0
        for byte in self.Image_Data:
            if shift <= len(data):
                bits = H.get_bits(byte)
                new_bits = bits[:-self.Bits_to_rewrite_count] \
                           + data[shift:self.Bits_to_rewrite_count + shift]
                shift += self.Bits_to_rewrite_count
                img.write(bytes([int(new_bits, 2)]))
            else:
                img.write(bytes([byte]))

        img.close()

    def new_image(self, data):
        img = open(os.path.dirname(self.Path) + '/Combined image.bmp', 'wb')
        img.write(self.Head)
        shift = 0
        for byte in self.Image_Data:
            if shift < len(data):
                bits = H.get_bits(byte)
                new_bits = bits[:-self.Bits_to_rewrite_count] \
                           + data[shift:self.Bits_to_rewrite_count + shift] \
                           + ('0' * 8)
                new_bits = new_bits[:8]
                shift += self.Bits_to_rewrite_count
                img.write(bytes([int(new_bits, 2)]))
            else:
                img.write(bytes([byte]))

        img.close()
