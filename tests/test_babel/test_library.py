import pytest
from pathlib import Path

from babel.babel import Page, get_page, InvalidPageException


def test_valid_hexagon():
	assert Page.valid_hexagon("0")
	assert Page.valid_hexagon("abcd")
	assert Page.valid_hexagon("1234abcd")
	assert not Page.valid_hexagon("")
	assert not Page.valid_hexagon("asdgj.dsfoi")
	assert not Page.valid_hexagon("åäö")

def test_valid_wall():
	assert Page.valid_wall(4)
	assert Page.valid_wall(1)
	assert not Page.valid_wall(5)
	assert not Page.valid_wall(0)

def test_valid_shelf():
	assert Page.valid_shelf(5)
	assert Page.valid_shelf(1)
	assert not Page.valid_shelf(6)
	assert not Page.valid_shelf(0)

def test_valid_volume():
	assert Page.valid_volume(32)
	assert Page.valid_volume(1)
	assert not Page.valid_volume(33)
	assert not Page.valid_volume(0)

def test_valid_page():
	assert Page.valid_page(410)
	assert Page.valid_page(1)
	assert not Page.valid_page(411)
	assert not Page.valid_page(0)

def test_valid_page(valid_page):
	assert valid_page.valid_location()

def test_invalid_page(invalid_page):
	assert not invalid_page.valid_location()

def test_page_str():
	assert str(Page("0", 1, 1, 1, 1)) == "0-w1-s1-v1:1"
	assert str(Page("0123456789", 10, 20, 30, 40)) == "0123456789-w10-s20-v30:40"
	assert str(Page("12345678910", 1, 2, 3, 4)) == "12345...78910-w1-s2-v3:4"

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

def test_get_page_no_request(mocker, valid_page):
	"""Test the get_page function (no request sent)"""

	# Create mock object
	this_dir = Path(__file__).parent
	with open(this_dir / 'test_response.html', 'r') as f:
		test_response = f.read()

	response_mocker = mocker.Mock()
	response_mocker.text = test_response

	request_mocker = mocker.patch(
		'babel.babel.requests.post',
		return_value=response_mocker
	)

	# Test
	response = get_page(valid_page)

	assert response.startswith("e,ktdo.baefq ,z unqusiug..mvgxwni.ghyrharszlowrwmk")

	request_mocker.assert_called_once_with(
		'https://libraryofbabel.info/book.cgi',
		data={
			'hex': "0",
			'wall': 1,
			'shelf': 1,
			'volume': 1,
			'page': 1
		}
	)





