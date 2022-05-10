def inrange(x: float, a: float, b: float) -> bool:
	"""
	Check if a <= x <= b
	"""
	return a <= x <= b

def isint(x):
	"""Check if x is an integer"""
	return isinstance(x, int)