from ._error import StrError, SubClassError
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

        if not isinstance(string, str):
            raise StrError(string)

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

    def __init_subclass__(cls, **kwargs):
        raise SubClassError(cls)

    def __getitem__(self, item):
        i = Int_(item)
        return self.__string[i.int_]

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
        if not isinstance(new_value, str):
            raise StrError(new_value)

        self.__string = new_value

