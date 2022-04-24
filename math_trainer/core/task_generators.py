from abc import abstractmethod
from decimal import Decimal
import random
from typing import final, Optional, Union

from .import utilites



class MathTask:
    '''
    Base class for all generators of mathematical exercises
    '''

    def __init__(self) -> None:
        self._current_expression = self._generate_expression()


    @property
    def expression(self) -> str:
        return self._current_expression


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
    __current_operator: str
    __numbers: tuple[Union[int, Decimal], ...]

    def __init__(self, numberType: Optional[str]=None) -> None:
        self.__number_type = numberType
        super().__init__()


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
        nm1 = self.__get_number(self.__get_number_type())
        nm2 = self.__get_number(self.__get_number_type())
        self.__current_operator = self.__get_operator()
        if self.__current_operator == '/' and (isinstance(nm1, int) and isinstance(nm2, int)):
            nm1 *= nm2
        self.__numbers = (nm1, nm2,)
        return template.format(nm1, self.__current_operator, nm2)


    def check_result(self, expected_result: str) -> bool:
        '''
        Checks correctness of the passed result of the arithmetic expression calculation
        '''
        arithmetic_function = utilites.ARITHMETIC_FUNCTIONS[self.__current_operator]
        real_result = arithmetic_function(*self.__numbers)
        return expected_result == str(real_result)



@final
class QuadraticEquationTask(MathTask):
    '''
    Implement generation of quadratic equations
    '''

    def __init__(self) -> None:
        self.__roots = (utilites.get_random_int(1, 5), utilites.get_random_int(1, 5))
        super().__init__()


    def _generate_expression(self) -> str:
        template = 'x^2 {}x + {} = 0'
        coefficient = - (self.__roots[0] + self.__roots[1])
        constant_term = self.__roots[0] * self.__roots[1]
        return template.format(coefficient, constant_term)


    def check_result(self, expected_result: str) -> bool:
        root_candedates = tuple(map(int, expected_result.split(',')))
        if root_candedates[0] == self.__roots[0] and root_candedates[1] == self.__roots[1]:
            return True
        elif root_candedates[1] == self.__roots[0] and root_candedates[0] == self.__roots[1]:
            return True
        else:
            return False
