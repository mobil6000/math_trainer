from decimal import Decimal
from fractions import Fraction
import random
from time import sleep

import pytest

import utilites



class TestNumbers:

	def setup(self):
		self.range = random.sample(range(1, 11), 2)
		if self.range[0] > self.range[1]: self.range.reverse()


	def test_generate_integer(self):
		num = utilites.generate_integer(self.range)
		assert isinstance(num, int)
		assert self.range[0] <= num <= self.range[1]


	def test_generate_decimal(self):
		num = utilites.generate_decimal(self.range)
		assert isinstance(num, Decimal)
		integer_point = num.as_tuple()[1][0]
		assert self.range[0] <= integer_point <= self.range[1]


	def test_generate_fraction(self):
		num = utilites.generate_fraction(self.range)
		assert isinstance(num, Fraction)


	@pytest.mark.parametrize("func", [utilites.generate_integer, utilites.generate_fraction])
	def test_incorrect_argument_order(self, func):
		try:
			func([1, 0])
		except ValueError:
			pytest.fail('Unexpected ValuError')



class TestTimeMeter:
	__sleep_seconds = 3

	def setup(self):
		self.time_object = utilites.TimeMeter()


	def test_measurement(self):
		self.time_object.start()
		sleep(self.__sleep_seconds)
		result = self.time_object.finish()
		assert result is not None
		assert result == self.__sleep_seconds


	def test_finish_measurement_without_starting(self):
		with pytest.raises(NotImplementedError):
			self.time_object.finish()

