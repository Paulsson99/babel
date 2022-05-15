import requests
import string
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import TypeVar
from pathlib import Path

from . import utils


# CONSTANTS
URL = "https://libraryofbabel.info"
GET_PAGE_URL = "/book.cgi"
SEARCH_TEXT_URL = "/search.cgi"

CHAR_SET_TEXT = string.ascii_lowercase + ' ,.'
CHAR_SET_HEXAGON = string.ascii_lowercase + string.digits

MAX_TEXT_LENGTH = 3200

# TYPING
P = TypeVar('P', bound='Page')


@dataclass
class Page:
	"""A class for a page"""
	hexagon: str
	wall: int
	shelf: int
	volume: int
	page: int

	def content(self) -> str:
		"""
		Get the contents of the page
		"""
		if not self.valid_location():
			raise InvalidPageException(f"{self.location()} is not a valid page")

		# Request the page from the internet
		request_url = URL + GET_PAGE_URL
		form = self.to_dict(hexagon_name='hex')
		response = requests.post(request_url, data=form)

		# Extract the contents of the page
		soup = BeautifulSoup(response.text, features="html.parser")
		return soup.find(id="textblock").get_text()

	def location(self) -> str:
		"""
		Return a string representing the location of the page
		This function returns a human readable string.
		For the exakt location use __repr__()
		"""
		hexagon_str = self.hexagon if len(self.hexagon) <= 10 else self.hexagon[:5] + '...' + self.hexagon[-5:]
		return f"{hexagon_str}-w{self.wall}-s{self.shelf}-v{self.volume}-p{self.page}"

	def valid_location(self) -> bool:
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
		return hexagon and utils.string.contains_only(hexagon, CHAR_SET_HEXAGON)

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
	def from_dict(clc, page_dict: dict) -> P:
		return clc(**page_dict)

	@classmethod
	def find(clc, text: str, location: int=0, padding=' ') -> P:
		"""Find a page with the exakt text 'text'"""
		text = text.lower()
		if not utils.string.contains_only(text, CHAR_SET_TEXT):
			raise InvalidPageTextException("Invalid text. It can only contain lowercase letters, space, period and comma")
		if len(text) + location > MAX_TEXT_LENGTH:
			raise InvalidPageTextException(f"Invalid text. Text lenght can´t exceed {MAX_TEXT_LENGTH}")
		if not padding is None and (len(padding) > 1 or not utils.string.contains_only(padding, CHAR_SET_TEXT)):
			raise InvalidPageTextException("Invalid padding. Can only be a lowercase character, space, period or comma")

		# Request the search from the internet
		request_url = URL + SEARCH_TEXT_URL
		form = {
			'find': clc._prepere_search_text(text, location, padding)
		}
		response = requests.post(request_url, data=form)

		# Extract the page location from the first a-tag
		soup = BeautifulSoup(response.text, features="html.parser")
		a_tag = soup.find('a')
		location_info = a_tag['onclick']

		raw_hexagon, raw_wall, raw_shelf, raw_volume, raw_page = location_info.split(',')

		# Remove extra characters
		hexagon = raw_hexagon[9:].strip("'")
		wall = raw_wall.strip("'")
		shelf = raw_shelf.strip("'")
		volume = raw_volume.strip("'")
		page = raw_page[:-1].strip("'")

		return clc(hexagon, int(wall), int(shelf), int(volume), int(page))

	@staticmethod
	def _prepere_search_text(text: str, location: int, padding: str):
		"""Pad the search string correctly"""
		if padding is None:
			padding_left = utils.string.random_string(length=location, char_set=CHAR_SET_TEXT)
			padding_right = utils.string.random_string(length=MAX_TEXT_LENGTH - location - len(text), char_set=CHAR_SET_TEXT)
			return padding_left + text + padding_right
		else:
			return utils.string.left_pad(
				utils.string.right_pad(
					text,
					padding=padding, 
					pad_size=MAX_TEXT_LENGTH - location - len(text)
				),
				padding=padding,
				pad_size=location
			)

	def to_dict(self, hexagon_name='hexagon') -> dict:
		return {
			hexagon_name: self.hexagon,
			'wall': self.wall,
			'shelf': self.shelf,
			'volume': self.volume,
			'page': self.page
		}

	def save(self, path):
		"""Save the book page"""
		save_path = Path(path) / (self.location() + '.txt')
		with open(save_path, 'w') as f:
			f.write(repr(self) + '\n')
			f.write(str(self))

	def __repr__(self) -> str:
		return f"{self.hexagon}-w{self.wall}-s{self.shelf}-v{self.volume}-p{self.page}"

	def __str__(self) -> str:
		return self.content()

	
class InvalidPageException(Exception):
	pass


class InvalidPageTextException(Exception):
	pass





