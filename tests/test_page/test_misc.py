import pytest
from babel.page import Page


def test_page_location():
	assert Page("0", 1, 1, 1, 1).location() == "0-w1-s1-v1:1"
	assert Page("0123456789", 10, 20, 30, 40).location() == "0123456789-w10-s20-v30:40"
	assert Page("12345678910", 1, 2, 3, 4).location() == "12345...78910-w1-s2-v3:4"

def test_page_repr():
	assert repr(Page("0", 1, 1, 1, 1)) == "0-w1-s1-v1:1"
	assert repr(Page("0123456789", 10, 20, 30, 40)) == "0123456789-w10-s20-v30:40"
	assert repr(Page("12345678910", 1, 2, 3, 4)) == "12345678910-w1-s2-v3:4"
