from typing import Type, Any, Iterable, final
from ._error import SetError, SetTypeError, SubClassError
from .Subclass import notSubclass

@notSubclass
@final
class Set_:

    def __init__(self, _set: set = set(), types: list[Type] = None):
        """
        Create immutable set type
        :param _set: A set
        :param types: All accepted types for the set
        """

        self.__types = types

        if not isinstance(_set, set):
            raise SetError(_set)

        self.__set = _set
        self.__check_types(_set)


    def __iter__(self):
        return iter(self.__set)

    def __bool__(self):
        return self.__set != set()

    def __eq__(self, other):
        return self.__set == other

    def __str__(self):
        return str(self.__set)

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __init_subclass__(cls, **kwargs):
        raise SubClassError(cls)

    def __check_types(self, value: set):

        if self.__types is None:
            self.__types = []
            for i in value:
                t = type(i)
                if t not in self.__types:
                    self.__types.append(t)
            if self.__types == []:
                self.__types = None
            return

        for i in value:
            t = type(i)
            if t not in self.__types:
                raise SetTypeError(self.__types, self.__set, i)

    def __check_type(self, value):

        if type(value) not in self.__types:
            raise SetTypeError(self.__types, self.__set, value)


    def add(self, value: Any) -> None:
        """
        Add a value
        :param value: Any value
        :return: None
        :raise SetTypeError:
        """
        self.__check_type(value)
        self.__set.add(value)

    def update(self, *s: Iterable) -> None:
        """
        Update a set with the union of itself and others.
        :param s: sets
        :return: None
        :raise SetTypeError:
        """
        for _set in s:
            self.__check_types(_set)

        self.__set.update(s)

    @property
    def set_(self) -> set:
        """
        Return actual value
        :return: set
        """
        return self.__set