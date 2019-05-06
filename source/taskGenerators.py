
class TaskFactory:

	def __init__(self, taskgen = None):
		self.__task_generator = taskgen
		self.__task_counter, self.__right_task_counter =0, 0


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
		return new_task


	def check_current_task(self, answer):
		self.__check_task_generator()
		retcode = self.__task_generator.check_answer(answer)
		if retcode: self.__right_task_counter +=1
		return retcode
