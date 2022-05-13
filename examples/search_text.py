from babel.page import Page

# Find a page with the contents 'Hello'
page = Page.find_text("Hello")

# Print the location of the page
print(page.location())

# Print the contents of the page
print(page)
