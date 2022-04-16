import decimal
import fractions
import random
import time
from typing import Optional



class TimeMeter:

	__slots__ = ('start_time', 'end_time')
	start_time: Optional[float]
	end_time: Optional[float]

	def __init__(self) -> None:
		self.__start_time, self.__end_time = None, None


	def start(self -> None):
		if self.__end_time is not None:
			self._end_time = None
		self.__start_time = time.monotonic()


	def finish(self) -> int:
		if self.__start_time is None:
			raise NotImplementedError('start point of time measurement is not defined')
		self.__end_time = time.monotonic()
		return int(self.__end_time - self.__start_time)



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
