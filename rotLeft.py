def rotLeft(a, d):
	"""

	>>> rotLeft([1, 2, 3, 4, 5], 4)
	[5, 1, 2, 3, 4]

	>>> rotLeft([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)
	[77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]
	"""

	if len(a) >= d:
		return a[d:] + a[:d]

	if len(a) == d:
		return a

	shift = len(a) % d

	if len(a) <= d and shift == 0:
		return a

	else:
		return a[-shift:] + a[:-shift]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)