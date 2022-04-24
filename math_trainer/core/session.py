from typing import final, Optional, Type, TypedDict

from .task_generators import MathTask
from .utilites import TimeMeter



class TrainingResult(TypedDict, total=False):
    task_counter: int
    right_task_counter: int
    training_time: int
    average_time: float
    percentage_of_correct_answers: int



@final
class TrainingSession:
    __current_task: MathTask
    __results: TrainingResult

    def __init__(
        self,
        task_generator: Type[MathTask],
        params: Optional[dict]=None,
        number_of_tasks: int = 10
    ) -> None:
        self.__number_of_tasks = number_of_tasks
        self.__task_generator = task_generator
        self.__generator_params = params
        self.__results = {'task_counter': 0, 'right_task_counter': 0}
        self.__time_meter = TimeMeter()
        self.__time_meter.start()


    @property
    def results(self) -> TrainingResult:
        return self.__results


    def generate_task(self) -> str:
        self.__results['task_counter'] += 1
        if self.__results['task_counter'] == self.__number_of_tasks:
            self.__results['training_time'] = self.__time_meter.finish()
            self.__compute_statistics()
            raise StopIteration
        if self.__generator_params is not None:
            self.__current_task = self.__task_generator(**self.__generator_params)
        else:
            self.__current_task = self.__task_generator()
        return self.__current_task.expression


    def check_task_result(self, answer: str) -> bool:
        result = self.__current_task.check_result(answer)
        if result:
            self.__results['right_task_counter'] += 1
        return result


    def __compute_statistics(self) -> None:
        self.__results['average_time'] = (
            self.__results['training_time'] / self.__results['task_counter']
        )
        self.__results['percentage_of_correct_answers'] = (
            int(self.__results['right_task_counter'] * 100 / self.__results['task_counter'])
        )



def make_report(data: TrainingResult) -> str:
    with open('math_trainer/report_template', 'r') as file_object:
        report = file_object.read().format(**data)
    return report
