import requests
import string
from bs4 import BeautifulSoup

from . import utils


class Library:
	"""
	Class for interacting with the library
	"""

	# URL to the library
	url = "https://libraryofbabel.info"

	GET_PAGE = "/book.cgi"

	def __init__(self):
		pass

	def get_page(self, hexagon: str, wall: int, shelf: int, volume: int, page: int) -> str:
		"""
		Get a page and return the contents of the page

		hex: str
		wall: int [1-4]
		shelf: int [1-5]
		volume: int [1-32]
		page: int [1-410]
		"""

		if not self.valid_hexagon(hexagon):
			raise ValueError(f"Hexagon '{hexagon}'' is not valid. It should only contain a-z or 0-9")
		if not self.valid_wall(wall):
			raise ValueError(f"Wall '{wall}' is not valid. It should be an int in the range 1-4")
		if not self.valid_shelf(shelf):
			raise ValueError(f"Shelf '{shelf}' is not valid. It shoud be an int int the range 1-5")
		if not self.valid_volume(volume):
			raise ValueError(f"Volume '{volume}' is not valid. It shoud be an int int the range 1-32")
		if not self.valid_page(page):
			raise ValueError(f"Page '{page}' is not valid. It shoud be an int int the range 1-410")

		request_url = self.url + self.GET_PAGE
		form = {
			'hex': hexagon,
			'wall': wall,
			'shelf': shelf,
			'volume': volume,
			'page': page
		}

		response = requests.post(request_url, data=form)

		soup = BeautifulSoup(response.text, features="html.parser")

		return soup.find(id="textblock").get_text()

		

	def valid_hexagon(self, hexagon: str) -> bool:
		"""Only abc...xyz and 0-9 are allowed and it should not be empty"""
		return hexagon and utils.string.contains_only(hexagon, string.ascii_lowercase + string.digits)

	def valid_wall(self, wall: int) -> bool:
		return utils.math.isint(wall) and utils.math.inrange(wall, 1, 4)

	def valid_shelf(self, shelf: int) -> bool:
		return utils.math.isint(shelf) and utils.math.inrange(shelf, 1, 5)

	def valid_volume(self, volume: int) -> bool:
		return utils.math.isint(volume) and utils.math.inrange(volume, 1, 32)

	def valid_page(self, page: int) -> bool:
		return utils.math.isint(page) and utils.math.inrange(page, 1, 410)





