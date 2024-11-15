from sys import maxsize
from typing import Any, final
from ._error import TupleError
from .Subclass import notSubclass

@notSubclass
@final
class Tuple_:

    def __init__(self, _tuple: tuple[Any]):
        """
        Create immutable tuple type
        :param _tuple: a tuple
        """

        self.__check_type(_tuple)

        self.__tuple = _tuple

    def __len__(self):
        return len(self.__tuple)

    def __bool__(self):
        return True if self.__tuple else False

    def __iter__(self):
        return iter(self.__tuple)

    def __str__(self):
        return str(self.__tuple)

    def __repr__(self):
        return f"Tuple({self.__tuple!r})"

    def __eq__(self, other):
        return self.__tuple == other

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __check_type(self, value):
        if not isinstance(value, (tuple, Tuple_)):
            raise TupleError(value)

    @property
    def tuple_(self) -> tuple:
        """
        Return actual value
        :return: tuple
        """
        return self.__tuple

    @tuple_.setter
    def tuple_(self, new_tuple):
        """
        Set a new value
        :param new_tuple: Any
        :return: None
        """
        self.__check_type(new_tuple)

        self.__tuple = new_tuple

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