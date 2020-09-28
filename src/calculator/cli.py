from argparse import Action, ArgumentParser

class ArithmeticAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        first, second = values
        namespace.a = int(first)
        namespace.b = int(second)
        setattr(namespace, self.dest, True)


def create_parser():
    parser = ArgumentParser(description="Calc - An arithemtic Calculator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--add","-a",help="Add two integers", action=ArithmeticAction,nargs=2)
    group.add_argument("--subtract","-s",help="Subtract two integers", action=ArithmeticAction,nargs=2)
    return parser


def main():
    args = create_parser().parse_args()
    print(args)
    if args.add:
        print(args.a + args.b)
    if args.subtract:
        print(args.a - args.b)
    

if __name__ == '__main__':
    main()