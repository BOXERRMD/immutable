from ._error import BoolError
from typing import final
from .Subclass import notSubclass

@notSubclass
@final
class Bool_:

    def __init__(self, boolean: bool) -> None:
        """
        Create immutable bool type
        :param boolean: a boolean
        """

        self.__check_type(boolean)

        self.__boolean = boolean

    def __str__(self):
        return str(self.__boolean)

    def __bool__(self):
        return self.__boolean

    def __eq__(self, other):
        return self.bool_ == other

    def __repr__(self):
        return f"Bool({self.__boolean!r})"

    def __and__(self, other):
        return self.__boolean & other

    def __or__(self, other):
        return self.__boolean | other

    def __int__(self):
        return int(self.bool_)

    def __check_type(self, value):
        if not isinstance(value, (bool, Bool_)):
            raise BoolError(value)

    @property
    def bool_(self) -> bool:
        """
        Return actual value
        :return: bool
        """
        return self.__boolean

    @bool_.setter
    def bool_(self, new_value):
        """
        Set a new value
        :param new_value: a boolean
        :return: None
        """
        self.__check_type(new_value)

        self.__boolean = new_value