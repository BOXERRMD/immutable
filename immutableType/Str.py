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
        """
        Return the initial string associated.
        :return: str
        """
        return self.__string

    def __len__(self):
        """
        Return the number of carter in the initial string.
        :return: int
        """
        return len(self.__string)

    def __bool__(self):
        """
        Return True if the initial string is not empty, else False.
        :return: bool
        """
        return True if self.__string else False

    def __repr__(self):
        return f"Str({self.__string!r})"

    def __iter__(self):
        """
        Return an iterable created on the initial string.
        :return: iterable
        """
        return iter(self.__string)

    def __eq__(self, other):
        """
        Return True if ``other`` and the initial string is equal, else False.
        :param other: another value
        :return: bool
        """
        return self.str_ == other

    def __and__(self, other):
        """
        Calked on __bool__ function, return True if __bool__ is True and ``other`` is True, else False.
        :param other: another boolean value
        :return: bool
        """
        return self.__bool__() == other

    def __or__(self, other):
        """
        Calked on __bool__ function, return True if __bool__ is True or ``other`` is True, else False.
        :param other: another boolean value
        :return: bool
        """
        return self.__bool__() != other

    def __getitem__(self, item: int):
        """
        Return the character associated of the initial string.
        :param item: int
        :return: a character from the initial string
        """
        i = Int_(item)
        return self.__string[i.int_]

    def __add__(self, other: str):
        """
        Add ``other`` at the initial string by the ``+`` operator.
        :param other: a string
        :return: Str_ class
        """
        self.__check_type(other)
        self.__string += other
        return self

    def __iadd__(self, other: str):
        """
                Add ``other`` at the initial string by the ``+`` operator.
                :param other: a string
                :return: Str_ class
                """
        return self.__add__(other)

    def __sub__(self, other: str):
        """
        Replace ``other`` string by ``''`` for 1 occurrence.
        :param other: a string
        :return: Str_ class
        """
        self.__check_type(other)
        self.__string = self.__string.replace(other, '', 1)
        return self

    def __isub__(self, other: str):
        """
                Replace ``other`` string by ``''`` for 1 occurrence.
                :param other: a string
                :return: Str_ class
                """
        return self.__sub__(other)

    def __check_type(self, value):
        if not isinstance(value, (str, Str_)):
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

