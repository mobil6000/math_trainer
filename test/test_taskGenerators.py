import pytest
import taskGenerators
from utilites import TimeMeter

from . import stubs



class TestSessionObject:

	@pytest.fixture()
	def session_without_task_generator(self):
		obj = taskGenerators.Session()
		return obj


	@pytest.fixture()
	def session_with_created_task(self):
		obj = taskGenerators.Session(stubs.FakeTaskGenerator())
		obj.create_new_task()
		return obj


	def setup(self):
		self.session_object = taskGenerators.Session(stubs.FakeTaskGenerator())


	def test_init_generator_object(self):
		assert self.session_object.task_counter == 0 and self.session_object.right_task_counter == 0
		assert isinstance(self.session_object.task_generator, stubs.FakeTaskGenerator)
		assert isinstance(self.session_object._Session__time_meter, TimeMeter)


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
