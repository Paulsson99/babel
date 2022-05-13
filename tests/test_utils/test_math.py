from pybel.utils.math import inrange, isint


def test_inrange_with_int():
	"""Test the inrange function with integers"""
	# Basic tests
	assert inrange(1, 0, 2)
	assert not inrange(3, 0, 2)

	# Negative numbers
	assert inrange(-1, -2, 3)
	assert not inrange(-2, -1, 0)

	# Exact value
	assert inrange(1, 1, 2)
	assert inrange(1, 1, 1)

def test_inrange_with_float():
	"""Test the inrange function with floats"""
	# Basic with floats
	assert inrange(1.0, 0.0, 2.0)
	assert not inrange(3.0, 0.0, 2.0)

	# Negative numbers
	assert inrange(-1.0, -2.0, 3.0)
	assert not inrange(-2.0, -1.0, 0.0)

	# Exact value
	assert inrange(1.0, 1.0, 2.0)
	assert inrange(1.0, 1.0, 1.0)

def test_isint():
	"""Test the isint function"""
	assert isint(1)
	assert not isint(1.0)

	assert isint(-1)