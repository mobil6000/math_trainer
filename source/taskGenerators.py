import abc



class TaskGenerator:
	__metaclass__ = abc.ABCMeta
	_task_counter, _right_task_counter =0, 0


	@property
	def task_counter(self):
		return self._task_counter


	@property
	def right_task_counter(self):
		return self._right_task_counter


	@abc.abstractmethod
	def _generate_task_string(self): pass


	def create_new_task(self):
		new_task = self._generate_task_string()
		self._task_counter +=1
		return new_task


	@abc.abstractmethod
	def _check_answer(self, value): pass


	def check_current_task(self, answer):
		retcode = self._check_answer(answer)
		if retcode: self._right_task_counter +=1
		return retcode
