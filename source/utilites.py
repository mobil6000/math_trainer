import decimal
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



def get_random_int(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    return random.randint(start, end)


def get_random_decimal(start: int, end: int) -> Decimal:
    decimal_places = random.choice((1, 2))
    float_num = round(random.uniform(start, end), decimal_places)
    return Decimal(str(float_num))
