import pytest
from babel.page import Page


def test_page_str():
	assert str(Page("0", 1, 1, 1, 1)) == "0-w1-s1-v1:1"
	assert str(Page("0123456789", 10, 20, 30, 40)) == "0123456789-w10-s20-v30:40"
	assert str(Page("12345678910", 1, 2, 3, 4)) == "12345...78910-w1-s2-v3:4"
