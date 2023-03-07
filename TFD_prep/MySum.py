def my_sum(num1: int, num2: int) -> int:
	"""
	Sum two number

	Pre-condition: num1 and num2 must be int
	Post-condition: return the sum of num1 and num2
	"""
	assert type(num1) == int
	assert type(num2) == int
	return num1 + num2
