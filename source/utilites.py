import random
import decimal
import fractions



def generate_integer(rng):
	if rng[0] > rng[1]: rng.reverse()
	return random.randint(*rng)


def generate_decimal(rng):
	decimal_places = random.choice([1, 2])
	float_num =round(random.uniform(*rng), decimal_places)
	return decimal.Decimal(str(float_num))


def generate_fraction(rng):
	if rng[0] > rng[1]: rng.reverse()
	numerator =generate_integer(rng)
	denominator =generate_integer(rng)
	if denominator == 0: denominator += 1
	return fractions.Fraction(numerator, denominator)
