from pybel.utils.math import in_range, is_int


def test_inrange_with_int():
	"""Test the inrange function with integers"""
	# Basic tests
	assert in_range(1, 0, 2)
	assert not in_range(3, 0, 2)

	# Negative numbers
	assert in_range(-1, -2, 3)
	assert not in_range(-2, -1, 0)

	# Exact value
	assert in_range(1, 1, 2)
	assert in_range(1, 1, 1)

def test_inrange_with_float():
	"""Test the inrange function with floats"""
	# Basic with floats
	assert in_range(1.0, 0.0, 2.0)
	assert not in_range(3.0, 0.0, 2.0)

	# Negative numbers
	assert in_range(-1.0, -2.0, 3.0)
	assert not in_range(-2.0, -1.0, 0.0)

	# Exact value
	assert in_range(1.0, 1.0, 2.0)
	assert in_range(1.0, 1.0, 1.0)

def test_isint():
	"""Test the isint function"""
	assert is_int(1)
	assert not is_int(1.0)

	assert is_int(-1)