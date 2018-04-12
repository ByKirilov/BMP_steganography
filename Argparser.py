import Extract
import Combine
import argparse


def combine(args):
    """
    Calling the method of combine
    :param args:
    """
    Combine.combine(
        args.image_path,
        args.text_path,
        args.key,
        args.bits_to_rewrite_count
        )


def extract(args):
    """
    Calling the method of extract
    :param args:
    """
    Extract.extract(args.image_path, args.key, args.bits_to_rewrite_count)


def parse_args():
    """
    Parsing arguments
    :return Parsed arguments:
    """
    parser = argparse.ArgumentParser(description='Steganography.\
                                     A program for disguising text inside\
                                     a picture and extracting text from\
                                     a picture. To use the program, prepare\
                                     a picture in BMP format and a text file.',
                                     epilog='(C)byKirilov, 2017')
    subparsers = parser.add_subparsers()
    parser_combine = subparsers.add_parser(
        'combine',
        help='Hides the text in the picture.'
        )
    parser_combine.add_argument('image_path', help='Path to image')
    parser_combine.add_argument('text_path', help='Path to text')
    parser_combine.add_argument('key', help='Encryption key')
    parser_combine.add_argument(
        'bits_to_rewrite_count',
        type=int,
        help='Number of rewritable bits'
        )
    parser_combine.set_defaults(func=combine)

    parser_extract = subparsers.add_parser(
        'extract',
        help='Extract text from the picture.'
        )
    parser_extract.add_argument('image_path', help='Path to image')
    parser_extract.add_argument('key', help='Encryption key')
    parser_extract.add_argument(
        'bits_to_rewrite_count',
        type=int,
        help='Number of rewritable bits'
        )
    parser_extract.set_defaults(func=extract)

    return parser.parse_args()
