import random


def contains_only(s: str, allowed: str) -> bool:
	"""Check if a string s only contains characters in the string allowed"""
	return all(char in allowed for char in s)


def left_pad(s: str, padding: str, pad_size: int) -> str:
	"""Left pad a string with the string padding"""
	return padding * pad_size + s


def right_pad(s: str, padding: str, pad_size: int) -> str:
	"""Right pad a string with the string padding"""
	return s + padding * pad_size


def random_string(length: int, char_set: str) -> str:
	return ''.join(random.choices(char_set, k=length))
