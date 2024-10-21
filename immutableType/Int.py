from ._error import IntError, SubClassError
from typing import final
from .Subclass import notSubclass

@notSubclass
@final
class Int_:
    def __init__(self, integer: int) -> None:
        """
        Create immutable int type
        :param integer: an integer
        """

        if not isinstance(integer, int):
            raise IntError(integer)

        self.__integer = integer

    @property
    def int_(self) -> int:
        """
        Return actual value
        :return: int
        """
        return self.__integer

    @int_.setter
    def int_(self, new_value):
        """
        Set a new value
        :param new_value: an integer
        :return: None
        """
        if not isinstance(new_value, int):
            raise IntError(new_value)
        self.__integer = new_value

    def __str__(self):
        return str(self.__integer)

    def __int__(self):
        return self.__integer

    def __bool__(self):
        return True if self.__integer else False

    def __repr__(self):
        return f"Int({self.__integer!r})"

    def __eq__(self, other):
        return self.__integer == other

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __init_subclass__(cls, **kwargs):
        raise SubClassError()