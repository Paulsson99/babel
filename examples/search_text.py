from pybel.page import Page

# Find a page with the contents 'Hello'
page = Page.find("Hello")

# Print the location of the page
print(page.location())

# Print the contents of the page
print(page)
