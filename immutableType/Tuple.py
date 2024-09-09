from sys import maxsize
from typing import Any

from ._error import TupleError
class Tuple_:

    def __init__(self, _tuple: tuple[Any]):

        if not isinstance(_tuple, tuple):
            raise TupleError(_tuple)

        self.__tuple = _tuple

    @property
    def tuple_(self) -> tuple:
        return self.__tuple

    @tuple_.setter
    def tuple_(self, new_tuple):
        if not isinstance(new_tuple, tuple):
            raise TupleError(new_tuple)

        self.__tuple = new_tuple

    def __str__(self):
        return str(self.__tuple)

    def __repr__(self):
        return f"Tuple({self.__tuple!r})"

    def index(self, __value, __start: int = 0, __stop: int = maxsize) -> int:
        """
        Returns the index of the first element with the specified value
        :param __value: Any
        :param __start: int
        :param __stop: int
        :return: int
        :raise: ValueError if the value is not present
        """
        return self.__tuple.index(__value, __start, __stop)

    def count(self, __value) -> int:
        """
        Returns the number of elements with the specified value
        :param value: Any
        :return: int
        """
        return self.__tuple.count(__value)