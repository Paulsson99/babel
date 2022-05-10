from babel.babel import Library

# Create a Library object
lib = Library()

# Get page 1 in volume 1 on shelf 1 on wall 1 in hexagon 0
print(lib.get_page(hexagon="0", wall=1, shelf=1, volume=1, page=1))