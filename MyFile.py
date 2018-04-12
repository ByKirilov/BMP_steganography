import hashlib
import os.path
import Helper as H
import sys

from AESCipher import AESCipher
from io import StringIO


class MyFile:
    def __init__(self, file_path, enc_key):
        self.Path = os.path.abspath(file_path)
        if not os.path.exists(self.Path):
            sys.exit('File does not exist!')
        if not os.path.isfile(self.Path):
            sys.exit(self.Path + ' - is not file!')

        try:
            file = open(file_path, 'rb')
        except Exception:
            sys.exit('Can not open file!')

        try:
            self.File_bytes = file.read()
        except Exception:
            sys.exit('Can not read file!')

        self.File_name = os.path.basename(self.Path)

        file_name_bytes = self.File_name.encode()

        if len(file_name_bytes) > 255:
            sys.exit('File name is too long!')

        self.File_name_len = bytes([len(file_name_bytes)])

        self.Hash_sum = hashlib.md5(self.File_bytes).hexdigest()

        byte_string = self.Hash_sum.encode() \
            + self.File_name_len \
            + file_name_bytes \
            + self.File_bytes

        cipher = AESCipher(enc_key)

        self.Encrypted_file = cipher.encrypt(byte_string.decode())

        # The maximum number that is placed in the block
        self._max_enc_file_size = 9999999999999999999999999999999

        size_enc_file = len(self.Encrypted_file)
        if size_enc_file > self._max_enc_file_size:
            sys.exit('File too large!')
        self.Encrypted_size = cipher.encrypt(str(size_enc_file))

        self.Finally_byte_string = self.Encrypted_size + self.Encrypted_file

        self.Finally_size = len(self.Finally_byte_string)

        self.Binary_string = self.get_binary_string()

        file.close()

    def get_binary_string(self):
        result = StringIO()
        for i in self.Finally_byte_string:
            result.write(H.get_bits(i))
        return result.getvalue()
