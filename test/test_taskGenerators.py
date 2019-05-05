import pytest
from . import stubs



object = stubs.FakeTaskGenerator()


def test_init_generator_object():
	obj = stubs.FakeTaskGenerator()
	assert obj.task_counter == 0 and obj.right_task_counter == 0


def test_make_task():
	assert object.create_new_task() == 'test string'


def test_increment_task_counter():
	start_value = object.task_counter
	object.create_new_task() 
	end_value = object.task_counter
	assert end_value > start_value
	assert end_value - start_value == 1


def test_check_current_task():
	pass