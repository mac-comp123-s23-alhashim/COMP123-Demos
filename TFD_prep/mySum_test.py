from mySum import *


def test_my_sum_positives():
	assert my_sum(1, 2) == 3


def test_my_sum_negatives():
	assert my_sum(-1, -2) == -3


def test_my_sum_zeros():
	assert my_sum(0, 0) == 0


def test_my_sum_mix():
	assert my_sum(2, -2) == 0
