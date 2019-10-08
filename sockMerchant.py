
def sockMerchant(n, ar):
	"""
	>>> n = 9
	>>> ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
	>>> sockMerchant(n, ar)
	3
	"""
	ar.sort()

	count = 0
	i = 0

	while i < n - 1:
		if ar[i] == ar[i + 1]:
			count += 1
			i += 2
		else:
			i += 1

	return count
