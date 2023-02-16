def sum(num1: int, num2: int) -> int:
	"""
	Sum two number

	Post-condition: return the sum of num1 and num2
	"""
	return num1 + num2


def test_sum_positives():
	assert sum(1, 2) == 3


def test_sum_negatives():
	assert sum(-1, -2) == -3


def test_sum_zeros():
	assert sum(0, 0) == 0


def test_sum_mix():
	assert sum(2, -2) == 0
