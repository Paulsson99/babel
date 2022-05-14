import sys
from argparse import ArgumentParser

from .page import Page


def get_page(args) -> Page:
	return Page(
		hexagon=args.hexagon,
		wall=args.wall,
		shelf=args.shelf,
		volume=args.volume,
		page=args.page
	)

def find_page(args) -> Page:
	return Page.find(args.text)


parser = ArgumentParser(prog='pybel', description="API for interacting with the library of Babel")
subparsers = parser.add_subparsers(help='subcommands')

# Get page parser
get_parser = subparsers.add_parser(
	'get', 
	help='Get contents of a page in the library', 
	description='Get contents of a page in the library'
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
	description='Find a page with the specified text'
)
find_parser.add_argument('text', type=str, help='text to search for')
find_parser.set_defaults(func=find_page)

# Print help if no arguments are given
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parse the arguments and call the correct function
args = parser.parse_args()
page = args.func(args)

print(page)

