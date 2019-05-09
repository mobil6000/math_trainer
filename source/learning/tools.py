import decimal

import utilites

from . import defines



class Session:

	def __init__(self, taskgen = None):
		self.__task_generator = taskgen
		self.__task_counter, self.__right_task_counter =0, 0
		self.__time_meter = utilites.TimeMeter()


	@property
	def task_counter(self):
		return self.__task_counter


	@property
	def right_task_counter(self):
		return self.__right_task_counter


	@property
	def task_generator(self):
		return self.__task_generator


	@task_generator.setter
	def task_generator(self, generator_obj):
		self.__task_generator = generator_obj


	def __check_task_generator(self):
		if self.__task_generator is None:
			raise NotImplementedError


	def create_new_task(self):
		self.__check_task_generator()
		new_task = self.__task_generator.generate_task()
		self.__task_counter +=1
		self.__time_meter.start()
		return new_task


	def check_current_task(self, answer):
		self.__check_task_generator()
		self.__time_meter.finish()
		retcode = self.__task_generator.check_answer(answer)
		if retcode: self.__right_task_counter +=1
		return retcode



class ArithmeticParser:

	def __init__(self, exp):
		self.__exp = '({})'.format(exp)
		self.__prev_token = None
		self.__operands, self.__operators = [], []
		self.__pos = 0


	def __drop(self):
		self.__prev_token = None
		self.__pos = 0
		if self.__operands: self.__operands.clear()
		if self.__operators: self.__operators.clear()


	def __is_operator(self, value):
		return value in defines.ARITHMETIC_OPERATORS.keys()


	def __is_decimal(self, number):
		try:
			decimal.Decimal(number)
			return True
		except decimal.InvalidOperation:
			return False


	def __get_operator_priority(self, operator):
		if not self.__is_operator(operator):
			raise Exception('Не найден оператор "{}"'.format(operator))
		return defines.ARITHMETIC_OPERATORS[operator][0]


	def __execute(self):
		if len(self.__operands) < 2: return
		a, b = self.__operands.pop(), self.__operands.pop()
		operator = self.__operators.pop()
		action = defines.ARITHMETIC_OPERATORS[operator][1]
		self.__operands.append(action(b, a))


	def __can_pop_operator(self, operator):
		if not self.__operators: return False
		head = self.__operators[-1]
		if not self.__is_operator(head): return False
		priority1 = self.__get_operator_priority(operator)
		priority2 = self.__get_operator_priority(head)
		return priority1 >= priority2


	def __read_number(self):
		result = ''
		point = 0
		value = self.__exp[self.__pos]
		while value.isdigit() or value == '.':
			if value == '.':
				point += 1
				if point > 1:
					raise Exception

			result += value
			self.__pos += 1
			value = self.__exp[self.__pos]
		return result


	def __get_token(self):
		for i in range(self.__pos, len(self.__exp)):
			value = self.__exp[i]
			if value.isdigit():
				return self.__read_number()
			else:
				self.__pos += 1
				return value


	def calculate(self):
		token = self.__get_token()
		while token:
			if token.isspace(): pass
			elif token.isdigit(): self.__operands.append(int(token))
			elif self.__is_decimal(token): self.__operands.append(decimal.Decimal(token))
			elif self.__is_operator(token):

				if self.__prev_token == '(' and (token == '+' or token == '-'):
					self.__operands.append(0)
				while self.__can_pop_operator(token):
					self.__execute()
				self.__operators.append(token)

			elif token == '(':
				self.__operators.append(token)
			elif token == ')':

				while self.__operators and self.__operators[-1] != '(':
					self.__execute()
				self.__operators.pop()

			self.__prev_token = token
			token = self.__get_token()

		if self.__operators or len(self.__operands) > 1:
			raise Exception('Неверное выражение: operands={}, functions={}'.format(self.__operands, self.__operators))
		result = self.__operands[0]
		self.__drop()
		return result
