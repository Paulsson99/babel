import sys
from argparse import ArgumentParser

from .page import Page, CHAR_SET_TEXT


def get_page(args) -> None:
    page = Page(
        hexagon=args.hexagon,
        wall=args.wall,
        shelf=args.shelf,
        volume=args.volume,
        page=args.page
    )
    # Handle other args
    if args.save:
        page.save(args.save)
    else:
        print(page)


def find_page(args) -> None:
    page = Page.find(
        ' '.join(args.text),
        location=args.location,
        padding=None if args.padding.lower() == 'random' else args.padding.lower()
    )
    # Handle other args
    if args.save:
        page.save(args.save)
    else:
        print(page.location())
        if args.full:
            print(page)


parser = ArgumentParser(prog='pybel', description="API for interacting with the library of Babel")

save_parser = ArgumentParser(add_help=False)
save_parser.add_argument('--save', '-s', type=str, help='Location to save the page at')

subparsers = parser.add_subparsers(help='subcommands')

# Get page parser
get_parser = subparsers.add_parser(
    'get',
    help='Get contents of a page in the library',
    description='Get contents of a page in the library',
    parents=[save_parser]
)
get_parser.add_argument('hexagon', type=str, help='Hexagon in the library')
get_parser.add_argument('wall', type=int, help='Wall in the hexagon')
get_parser.add_argument('shelf', type=int, help='Shelf on the wall')
get_parser.add_argument('volume', type=int, help='Volume on the shelf')
get_parser.add_argument('page', type=int, help='Page in the volume')
get_parser.set_defaults(func=get_page)

# Find page parser
find_parser = subparsers.add_parser(
    'find',
    help='Find a page with the specified text',
    description='Find a page with the specified text',
    parents=[save_parser]
)
find_parser.add_argument('text', type=str, nargs='+', help='text to search for')
find_parser.add_argument('--location', '-l',
                         type=int,
                         default=0,
                         help='Location of the text on the page. Defaults to 0'
                         )
find_parser.add_argument('--padding', '-p',
                         type=str,
                         default=' ',
                         choices=list(CHAR_SET_TEXT) + ['random'],
                         help=f"Padding of the text. Can be one of the following '{CHAR_SET_TEXT}' or random. "
                              f"Defaults to ' ' "
                         )
find_parser.add_argument('--full', '-f', action='store_true', help='Show page')
find_parser.set_defaults(func=find_page)

# Print help if no arguments are given
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parse the arguments and call the correct function
args = parser.parse_args()
args.func(args)
