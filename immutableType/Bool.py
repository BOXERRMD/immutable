from ._error import BoolError, SubClassError
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

        if not isinstance(boolean, bool):
            raise BoolError(boolean)

        self.__boolean = boolean

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
        if not isinstance(new_value, bool):
            raise BoolError(new_value)

        self.__boolean = new_value

    def __str__(self):
        return str(self.__boolean)

    def __bool__(self):
        return self.__boolean

    def __eq__(self, other):
        return self.bool_ == other

    def __repr__(self):
        return f"Bool({self.__boolean!r})"

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __init_subclass__(cls, **kwargs):
        raise SubClassError(cls)