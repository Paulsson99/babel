import pytest
from babel.page import Page, get_page, find_text, InvalidPageException, InvalidPageTextException


def test_get_page_error_handling():
	"""Test the error handling in the get_page function"""
	with pytest.raises(InvalidPageException):
		get_page(Page("", 1, 1, 1, 1))
	with pytest.raises(InvalidPageException):
		get_page(Page("0", 0, 1, 1, 1))
	with pytest.raises(InvalidPageException):
		get_page(Page("0", 1, 0, 1, 1))
	with pytest.raises(InvalidPageException):
		get_page(Page("0", 1, 1, 0, 1))
	with pytest.raises(InvalidPageException):
		get_page(Page("0", 1, 1, 1, 0))

def test_find_text_error_handling():
	"""Test the error handling of find_text()"""
	with pytest.raises(InvalidPageTextException):
		find_text("123")
	with pytest.raises(InvalidPageTextException):
		find_text("a"*3201)
