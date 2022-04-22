from typing import final, Generator, Optional, TypedDict

from .task_generators import MathTask
from .utilites import TimeMeter



class TrainingResult(TypedDict, total=False):
    task_counter: int
    right_task_counter: int
    time_for_all_tasks: int
    time_for_every_task: list[tuple[int, int]]
    average_time: float
    percentage_of_correct_answers: int



@final
class TrainingSession:
    __current_task: MathTask
    __results: TrainingResult

    def __init__(self, task_generator, params: Optional[dict], number_of_tasks: int = 10) -> None:
        self.__number_of_tasks = number_of_tasks
        self.__task_generator = task_generator
        self.__generator_params = params
        self.__results = {'task_counter': 0, 'right_task_counter': 0}
        self.__time_meter = TimeMeter()
        self.__task_time_meter = TimeMeter()
        self.__time_meter.start()


    @property
    def results(self) -> TrainingResult:
        return self.__results


    def generate_task(self) -> Generator:
        while self.__results['task_counter'] <= self.__number_of_tasks:
            if self.__generator_params is not None:
                self.__current_task = self.__task_generator(**self.__generator_params)
            else:
                self.__current_task = self.__task_generator()
            self.__task_time_meter.start()
            yield self.__current_task.expression


    def check_task_result(self, answer: str) -> bool:
        self.__results['task_counter'] += 1
        time_for_solving_task = self.__task_time_meter.finish()
        result = self.__current_task.check_result(answer)
        if result:
            self.__results['right_task_counter'] += 1
        self.__results['time_for_every_task'].append(
            (self.__results['task_counter'], time_for_solving_task)
        )
        return result
