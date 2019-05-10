import random

import utilites

from .tools import ArithmeticParser
from .defines import *



class ArithmeticGenerator:

	def __init__(self, numberType, sign = None):
		self.__number_type = numberType
		self.__operator = sign
		self.__current_expression = ''
		self.__operands, self.__operators = [], []


	def __drop(self):
		if self.__current_expression: self.__current_expression = ''
		if self.__operands: self.__operands.clear()
		if self.__operators: self.__operators.clear()


	def __get_number_type(self):
		if self.__number_type is not None: return self.__number_type
		else: return random.choice(NUMBER_TYPES)


	def __get_operator(self):
		if self.__operator is not None: return self.__operator
		else: return random.choice(list(ARITHMETIC_OPERATORS.keys()))


	def __get_number(self, nType):
		if nType == 'integer': return utilites.generate_integer([1, 10])
		elif nType == 'decimal': return utilites.generate_decimal([1, 10])
		elif nType == 'fraction': return utilites.generate_fraction([1, 10])


	def __make(self, nm):
		for i in range(nm + 1):
			number_type = self.__get_number_type()
			self.__operands.append(self.__get_number(number_type))
			if i != nm:
				self.__operators.append(self.__get_operator())

		return 12


	def generate_task(self):
		actions = random.randint(1, 5)
		self.__current_expression = self.__make(actions)
		return '{} =?'.format(self.__current_expression)

