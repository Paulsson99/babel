from pybel import utils
from pybel.page import Page


def test_find_text_no_request(mocker_search_response, test_page_from_search):
	"""Test the find_text function (no request sent)"""
	page = Page.find("This is a test")
	assert page == test_page_from_search
	mocker_search_response.assert_called_once_with(
		'https://libraryofbabel.info/search.cgi',
		data={
			'find': utils.string.left_pad(
				utils.string.right_pad(
					"this is a test",  
					padding=' ', 
					pad_size=3200 - len("this is a test")
				),
				padding=' ',
				pad_size=0
			)
		}
	)


def test_get_page_no_request(mocker_page_response, valid_page):
	"""Test the get_page function (no request sent)"""
	response = valid_page.content()
	assert response.startswith("e,ktdo.baefq ,z unqusiug..mvgxwni.ghyrharszlowrwmk")
	mocker_page_response.assert_called_once_with(
		'https://libraryofbabel.info/book.cgi',
		data={
			'hex': "0",
			'wall': 1,
			'shelf': 1,
			'volume': 1,
			'page': 1
		}
	)
