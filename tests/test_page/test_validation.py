import pytest
from pybel.page import Page


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
