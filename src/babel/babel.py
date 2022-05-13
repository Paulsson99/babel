import requests
import string
from bs4 import BeautifulSoup
from dataclasses import dataclass

from . import utils


# CONSTANTS
URL = "https://libraryofbabel.info"
GET_PAGE_URL = "/book.cgi"
SEARCH_TEXT_URL = "/search.cgi"


@dataclass
class Page:
	"""A class for a page"""
	hexagon: str
	wall: int
	shelf: int
	volume: int
	page: int

	def valid_location(self):
		return (
			Page.valid_hexagon(self.hexagon) and 
			Page.valid_wall(self.wall) and
			Page.valid_shelf(self.shelf) and 
			Page.valid_volume(self.volume) and
			Page.valid_page(self.page)
		)

	@staticmethod
	def valid_hexagon(hexagon: str) -> bool:
		"""Only abc...xyz and 0-9 are allowed and it should not be empty"""
		return hexagon and utils.string.contains_only(hexagon, string.ascii_lowercase + string.digits)

	@staticmethod
	def valid_wall(wall: int) -> bool:
		return utils.math.isint(wall) and utils.math.inrange(wall, 1, 4)

	@staticmethod
	def valid_shelf(shelf: int) -> bool:
		return utils.math.isint(shelf) and utils.math.inrange(shelf, 1, 5)

	@staticmethod
	def valid_volume(volume: int) -> bool:
		return utils.math.isint(volume) and utils.math.inrange(volume, 1, 32)

	@staticmethod
	def valid_page(page: int) -> bool:
		return utils.math.isint(page) and utils.math.inrange(page, 1, 410)

	@classmethod
	def from_dict(clc, page_dict: dict):
		return clc(*page_dict)

	def to_dict(self) -> dict:
		return {
			'hex': self.hexagon,
			'wall': self.wall,
			'shelf': self.shelf,
			'volume': self.volume,
			'page': self.page
		}

	def __str__(self):
		hexagon_str = self.hexagon if len(self.hexagon) <= 10 else self.hexagon[:5] + '...' + self.hexagon[-5:]
		return f"{hexagon_str}-w{self.wall}-s{self.shelf}-v{self.volume}:{self.page}"


def get_page(page: Page) -> str:
	"""
	Get a page and return the contents of the page
	"""

	if not page.valid_location():
		raise InvalidPageException(f"{page} is not a valid page")

	request_url = URL + GET_PAGE_URL
	form = page.to_dict()

	response = requests.post(request_url, data=form)

	soup = BeautifulSoup(response.text, features="html.parser")

	return soup.find(id="textblock").get_text()

def find_text(text: str) -> Page:
	"""Find a page with the exakt text 'text'"""
	text = text.lower()
	if not utils.string.contains_only(text, string.ascii_lowercase + ' ,.'):
		raise InvalidPageTextException("Invalid text. It can only contain lowercase letters, space, period and comma")
	if len(text) > 3200:
		raise InvalidPageTextException("Invalid text. Text lenght can´t exceed 3200")

	request_url = URL + SEARCH_TEXT_URL
	form = {
		'find': text
	}

	response = requests.post(request_url, data=form)
	soup = BeautifulSoup(response.text, features="html.parser")

	# Get the first a tag on the page
	a_tag = soup.find('a')

	# Get text with link information
	location_info = a_tag['onclick']

	# Split the info
	raw_hexagon, raw_wall, raw_shelf, raw_volume, raw_page = location_info.split(',')

	# Remove extra characters
	hexagon = raw_hexagon[9:].strip("'")
	wall = raw_wall.strip("'")
	shelf = raw_shelf.strip("'")
	volume = raw_volume.strip("'")
	page = raw_page[:-1].strip("'")

	return Page(hexagon, int(wall), int(shelf), int(volume), int(page))

		
class InvalidPageException(Exception):
	pass

class InvalidPageTextException(Exception):
	pass





