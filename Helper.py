def bytes_to_int(bytes):
    """
    Translating a hexadecimal integer into a decimal number system
    :param bytes:
    """
    result = 0
    for i in range(len(bytes) - 1, -1, -1):
        result *= (16 ** ((i + 1) * 2))
        result += bytes[i]
    return result


def get_bits(int):
    """
    Getting an integer from 0 to 255 in a binary representation with
    insignificant zeros to length 8
    :param int:
    """
    if not 0 <= int <= 255:
        raise ValueError
    result = bin(int)[2:]
    if len(result) < 8:
        result = (8 - len(result)) * '0' + result

    return result