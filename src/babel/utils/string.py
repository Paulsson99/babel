def contains_only(s: str, allowed: str) -> bool:
	"""Check if a string s only contains characters in the string allowed"""
	return all(char in allowed for char in s)