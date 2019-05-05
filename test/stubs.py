from taskGenerators import *



class FakeTaskGenerator(TaskGenerator):

	def _generate_task_string(self):
		return 'test string'


	def _check_answer(self, value):
		return value.isdigit()
