from ._error import StrError
from .Int import Int_
from typing import final
from .Subclass import notSubclass

@notSubclass
@final
class Str_:
    def __init__(self, string: str) -> None:
        """
        Create immutable str type
        :param string: a string
        """

        self.__check_type(string)

        self.__string = string

    def __str__(self):
        return self.__string

    def __len__(self):
        return len(self.__string)

    def __bool__(self):
        return True if self.__string else False

    def __repr__(self):
        return f"Str({self.__string!r})"

    def __iter__(self):
        return iter(self.__string)

    def __eq__(self, other):
        return self.str_ == other

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __getitem__(self, item: int):
        i = Int_(item)
        return self.__string[i.int_]

    def __add__(self, other: str):
        self.__check_type(other)
        self.__string += other
        return self

    def __iadd__(self, other: str):
        return self.__add__(other)

    def __sub__(self, other: str):
        self.__check_type(other)
        self.__string = self.__string.replace(other, '', 1)
        return self

    def __isub__(self, other: str):
        return self.__sub__(other)

    def __check_type(self, value):
        if not isinstance(value, str):
            raise StrError(value)

    @property
    def str_(self) -> str:
        """
        Return actual value
        :return: str
        """
        return self.__string

    @str_.setter
    def str_(self, new_value):
        """
        Set a new value
        :param new_value: a string
        :return: None
        """
        self.__check_type(new_value)

        self.__string = new_value

