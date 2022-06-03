def in_range(x: float, a: float, b: float) -> bool:
	"""
	Check if a <= x <= b
	"""
	return a <= x <= b


def is_int(x: object) -> bool:
	"""Check if x is an integer"""
	return isinstance(x, int)
