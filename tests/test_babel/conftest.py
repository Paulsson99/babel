import pytest

from babel.babel import Page


@pytest.fixture
def valid_page():
	return Page(
		hexagon="0",
		wall=1,
		shelf=1,
		volume=1,
		page=1
	)

@pytest.fixture
def invalid_page():
	return Page(
		hexagon="0",
		wall=-1,
		shelf=666,
		volume=69,
		page=420
	)