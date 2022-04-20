from abc import abstractmethod
from decimal import Decimal
import random
from typing import final, Union

from .import utilites



class MathTask:
    '''
    Base class for all generators of mathematical exercises
    '''

    def __init__(self) -> None:
        self.__current_expression = self._generate_expression()


    @property
    def expression(self) -> str:
        return self.__current_expression


    @abstractmethod
    def _generate_expression(self) -> str:
        '''
        implements an algorithm for generating mathematical expressions.
        this method must be overridden in child classes.
        '''
        pass


    @abstractmethod
    def check_result(self, expected_result: str) -> bool:
        '''
        Checks correctness of the passed result of the expression calculation.
        this method must be overridden in child classes.
        '''
        pass



@final
class ArithmeticTask(MathTask):
    '''
    Implements generator of arithmetic tasks
    '''

    __NUMBER_TYPES = ('integer', 'decimal',)
    __OPERATORS = ('+', '-', '*', '/',)

    def __init__(self, numberType: str,) -> None:
        self.__number_type = numberType
        super()._generate_expression()


    def __get_number_type(self) -> str:
        if self.__number_type is not None:
            return self.__number_type
        else:
            return random.choice(self.__NUMBER_TYPES)


    def __get_operator(self) -> str:
        return random.choice(self.__OPERATORS)


    def __get_number(self, nType) -> Union[int, Decimal]:
        if nType == 'integer':
            return utilites.get_random_int(1, 10)
        else:
            return utilites.get_random_decimal(1, 10)


    def _generate_expression(self) -> str:
        '''
        Generates an arithmetic expression.
        '''
        template = '{0} {1} {2} =?'
        operand1 = self.__get_number(self.__get_number_type())
        operand2 = self.__get_number(self.__get_number_type())
        operator = self.__get_operator()
        return template.format(operand1, operator, operand2)


    def check_result(self, expected_result: str) -> bool:
        '''
        Checks correctness of the passed result of the arithmetic expression calculation
        '''
        real_result = eval(self.__current_expression[:-3])
        return int(expected_result) == real_result
