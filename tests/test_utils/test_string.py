from pybel.utils.string import contains_only, left_pad, right_pad, random_string


def test_contains_only():
	"""Test the function contains_only"""
	assert contains_only("12345", "1234567890")
	assert contains_only("abcd", "abcdefg")
	assert contains_only("123abcd", "123abcd")

	assert not contains_only("1234", "123abcd")
	assert not contains_only("abcd", "123")

def test_left_pad():
	assert left_pad("abc", padding='a', pad_size=3) == "aaaabc"
	assert left_pad("abc", padding='ab', pad_size=3) == "ababababc"
	assert left_pad("abc", padding='a', pad_size=0) == "abc"
	assert left_pad("abc", padding=' ', pad_size=3) == "   abc"

def test_right_pad():
	assert right_pad("abc", padding='a', pad_size=3) == "abcaaa"
	assert right_pad("abc", padding='ab', pad_size=3) == "abcababab"
	assert right_pad("abc", padding='a', pad_size=0) == "abc"
	assert right_pad("abc", padding=' ', pad_size=3) == "abc   "

def test_random_string():
	assert random_string(length=100, char_set='a') == 'a' * 100
	assert len(random_string(length=100, char_set='abc')) == 100
	assert random_string(length=0, char_set='abc') == ''
	assert set(random_string(length=100, char_set='ab')) == set(('a', 'b'))