import random
from decimal import Decimal
from fractions import Fraction
import pytest
import utilites



def create_new_range():
	while True:
		tmp = random.sample(range(1, 11), 2)
		if tmp[0] < tmp[1]:
			break
	return tmp


def test_generate_integer():
	rng = create_new_range()
	num = utilites.generate_integer(rng)
	assert isinstance(num, int)


def test_range_for_integers():
	rng = create_new_range()
	num = utilites.generate_integer(rng)
	assert rng[0] <= num <= rng[1]


def test_generate_decimal():
	rng = create_new_range()
	num = utilites.generate_decimal(rng)
	assert isinstance(num, Decimal)


def test_range_for_decimal():
	rng = create_new_range()
	num = utilites.generate_decimal(rng)
	integer_point = num.as_tuple()[1][0]
	assert rng[0] <= integer_point <= rng[1]


def test_generate_fraction():
	rng = create_new_range()
	num = utilites.generate_fraction(rng)
	assert isinstance(num, Fraction)


@pytest.mark.parametrize("func", [utilites.generate_integer, utilites.generate_fraction])
def test_incorrect_argument_order(func):
	try:
		func([1, 0])
	except ValueError:
		pytest.fail('Unexpected ValuError ..')
