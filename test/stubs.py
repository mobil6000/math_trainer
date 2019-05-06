
class FakeTaskGenerator:

	def generate_task(self):
		return 'test string'


	def check_answer(self, value):
		return value.isdigit()
