import Argparser

if __name__ == '__main__':
    args = Argparser.parse_args()
    args.func(args)
