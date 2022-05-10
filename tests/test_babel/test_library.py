import pytest
from pathlib import Path
from babel.babel import Library


def test_valid_hexagon(library):
	assert library.valid_hexagon("0")
	assert library.valid_hexagon("abcd")
	assert library.valid_hexagon("1234abcd")
	assert not library.valid_hexagon("")
	assert not library.valid_hexagon("asdgj.dsfoi")
	assert not library.valid_hexagon("åäö")

def test_valid_wall(library):
	assert library.valid_wall(4)
	assert library.valid_wall(1)
	assert not library.valid_wall(5)
	assert not library.valid_wall(0)

def test_valid_shelf(library):
	assert library.valid_shelf(5)
	assert library.valid_shelf(1)
	assert not library.valid_shelf(6)
	assert not library.valid_shelf(0)

def test_valid_volume(library):
	assert library.valid_volume(32)
	assert library.valid_volume(1)
	assert not library.valid_volume(33)
	assert not library.valid_volume(0)

def test_valid_page(library):
	assert library.valid_page(410)
	assert library.valid_page(1)
	assert not library.valid_page(411)
	assert not library.valid_page(0)

def test_get_page_error_handling(library):
	"""Test the error handling in the get_page function"""
	with pytest.raises(ValueError):
		library.get_page("", 1, 1, 1, 1)
	with pytest.raises(ValueError):
		library.get_page("0", 0, 1, 1, 1)
	with pytest.raises(ValueError):
		library.get_page("0", 1, 0, 1, 1)
	with pytest.raises(ValueError):
		library.get_page("0", 1, 1, 0, 1)
	with pytest.raises(ValueError):
		library.get_page("0", 1, 1, 1, 0)

def test_get_page_no_request(mocker, library):
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
	response = library.get_page("0", 1, 1, 1, 1)

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





