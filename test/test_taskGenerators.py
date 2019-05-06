import pytest

import taskGenerators
from utilites import TimeMeter
from . import stubs



object = taskGenerators.TaskFactory(stubs.FakeTaskGenerator())


def test_init_generator_object():
	obj = taskGenerators.TaskFactory()
	assert isinstance(obj._TaskFactory__time_meter, TimeMeter)
	assert obj.task_counter == 0 and obj.right_task_counter == 0


def test_make_task():
	task = object.create_new_task()
	assert task is not None
	assert task == 'test string'


def test_increment_task_counter():
	start_value = object.task_counter
	object.create_new_task() 
	end_value = object.task_counter
	assert end_value > start_value
	assert end_value - start_value == 1


def test_check_current_task():
	result = object.check_current_task('')
	assert result is not None
	assert result is False
	result = object.check_current_task('123')
	assert result is True


def test_increment_right_task_counter():
	start_value = object.right_task_counter
	object.check_current_task('123')
	end_value = object.right_task_counter
	assert end_value > start_value
	assert end_value - start_value == 1


def test_generate_task_without_generator():
	factory = taskGenerators.TaskFactory()
	with pytest.raises(NotImplementedError):
		factory.create_new_task()


def test_check_task_without_generator():
	factory = taskGenerators.TaskFactory()
	with pytest.raises(NotImplementedError):
		factory.check_current_task('')
