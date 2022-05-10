from utils.string import contains_only

def test_contains_only():
	"""Test the function contains_only"""
	assert contains_only("12345", "1234567890")
	assert contains_only("abcd", "abcdefg")
	assert contains_only("123abcd", "123abcd")

	assert not contains_only("1234", "123abcd")
	assert not contains_only("abcd", "123")