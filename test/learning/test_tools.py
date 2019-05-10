from decimal import Decimal
from fractions import Fraction
import pytest
from learning import tools
from utilites import TimeMeter

from test import stubs



class TestSessionObject:

	@pytest.fixture()
	def session_without_task_generator(self):
		obj = tools.Session()
		return obj


	@pytest.fixture()
	def session_with_created_task(self):
		obj = tools.Session(stubs.FakeTaskGenerator())
		obj.create_new_task()
		return obj


	def setup(self):
		self.session_object = tools.Session(stubs.FakeTaskGenerator())


	def test_init_generator_object(self):
		session_object = tools.Session(stubs.FakeTaskGenerator())
		assert session_object.task_counter == 0 and session_object.right_task_counter == 0
		assert isinstance(session_object.task_generator, stubs.FakeTaskGenerator)
		assert isinstance(session_object._Session__time_meter, TimeMeter)


	def test_make_task(self):
		task = self.session_object.create_new_task()
		assert task is not None
		assert task == 'test string'


	def test_increment_task_counter(self):
		start_value = self.session_object.task_counter
		self.session_object.create_new_task() 
		end_value = self.session_object.task_counter
		assert end_value > start_value
		assert end_value - start_value == 1


	def test_check_current_task(self, session_with_created_task):
		result = session_with_created_task.check_current_task('')
		assert result is not None
		assert result is False
		result = session_with_created_task.check_current_task('123')
		assert result is True


	def test_increment_right_task_counter(self, session_with_created_task):
		start_value = session_with_created_task.right_task_counter
		session_with_created_task.check_current_task('123')
		end_value = session_with_created_task.right_task_counter
		assert end_value > start_value
		assert end_value - start_value == 1


	def test_generate_task_without_generator(self, session_without_task_generator):
		with pytest.raises(NotImplementedError):
			session_without_task_generator.create_new_task()


	def test_check_task_without_generator(self, session_without_task_generator):
		with pytest.raises(NotImplementedError):
			session_without_task_generator.check_current_task('')



class TestArithmeticParser:

	@classmethod
	def setup_class(cls):
		cls.expressions = {
			'simple': ('17 + 14', 31), 
			'difficult': ('4 + 6 + 5 * 8', 50), 
			'brackets': ('14 -(5 + 4) +(13 + 5 * 2)', 28), 
			'decimal': ('4.2 + 3.3', Decimal('7.5')), 
			'fraction': ('4/5 + 1/2', Fraction('13/10'))
		}


	def test_calculate_simple_expression(self):
		parser = tools.ArithmeticParser(self.expressions['simple'][0])
		assert parser.calculate() == self.expressions['simple'][1]


	def test_operators_priority(self):
		parser = tools.ArithmeticParser(self.expressions['difficult'][0])
		assert parser.calculate() == self.expressions['difficult'][1]


	def test_calculate_with_brackets(self):
		parser = tools.ArithmeticParser(self.expressions['brackets'][0])
		assert parser.calculate() == self.expressions['brackets'][1]


	def test_calculate_with_decimal(self):
		parser = tools.ArithmeticParser(self.expressions['decimal'][0])
		assert parser.calculate() == self.expressions['decimal'][1]


	def test_calculate_with_fraction(self):
		parser = tools.ArithmeticParser(self.expressions['fraction'][0])
		assert parser.calculate() == self.expressions['fraction'][1]
