from decimal import Decimal
import random
from time import sleep

import pytest

import utilites



@pytest.fixture
def new_range() -> list[int]:
	numbers: list = random.sample(range(1, 16), 2)
	if numbers[0] > numbers[1]:
		numbers.reverse()
	return numbers


def test_get_random_int(new_range: list[int]):
	expected_result = utilites.get_random_int(*new_range)
	assert new_range[0] <= expected_result <= new_range[1]


def test_get_random_decimal(new_range: list[int]):
	expected_result = utilites.get_random_decimal(*new_range)
	integer_part = expected_result.as_tuple()[1][0]
	assert new_range[0] <= integer_part <= new_range[1]



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

