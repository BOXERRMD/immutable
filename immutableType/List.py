from sys import maxsize
from .Int import Int_
from ._error import ListError, ListTypeError
from typing import Any, Type, final
from .Subclass import notSubclass

@notSubclass
@final
class List_:

    def __init__(self, _list: list[Any] = [], types: list[Type] = None):
        """
        Create immutable list type
        :param _list: a list
        :param types: All accepted types for the list
        """

        self.__types = types

        self.__check_base_type(_list)

        self.__list = _list
        self.__check_types(_list)


    def __len__(self):
        return len(self.__list)

    def __getitem__(self, item: int):
        i = Int_(item)
        return self.__list[i.int_]

    def __bool__(self):
        return True if self.__list else False

    def __setitem__(self, key: int, value):

        self.__check_types([value])
        u = Int_(key)
        self.__list[u.int_] = value

    def __delitem__(self, key: int):
        u = Int_(key)
        del self.__list[u.int_]

    def __iter__(self):
        return iter(self.__list)

    def __eq__(self, other):
        return self.__list == other

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __str__(self):
        return str(self.__list)

    def __repr__(self):
        return f"List({self.__list!r})"

    def __add__(self, other: list):
        self.__check_base_type(other)

        self.__check_types(other)
        self.__list += other
        return self

    def __iadd__(self, other: list):
        return self.__add__(other)

    def __sub__(self, other: list):
        self.__check_base_type(other)
        self.__list = [i for i in self.__list if i not in other]
        return self

    def __isub__(self, other: list):
        return self.__sub__(other)

    def __check_types(self, value: list) -> None:
        """
        Look if all types is in self.__types
        :param value: iterable
        :return: None
        """
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
                raise ListTypeError(self.__types, self.__list, i)

    def __check_type(self, value):
        if type(value) not in self.__types:
            raise ListTypeError(self.__types, self.__list, value)

    def __check_base_type(self, value):
        if not isinstance(value, (list, List_)):
            raise ListError(value)

    @property
    def list_(self) -> list:
        """
        Return actual value
        :return: list
        """
        return self.__list

    @list_.setter
    def list_(self, new_list):
        """
        Set a new value
        :param new_value: Any
        :return: None
        """
        self.__check_base_type(new_list)

        self.__check_types(new_list)

        self.__list = new_list


    def append(self, __object) -> None:
        """
        Adds an element at the end of the list
        :param __object: Any
        :return: None
        """

        self.__check_type(__object)

        self.__list.append(__object)

    def clear(self) -> None:
        """
        Removes all the elements from the list
        :return: None
        """
        self.__list.clear()

    def copy(self) -> list:
        """
        Returns a copy of the list
        :return: list
        """
        return self.__list.copy()

    def count(self, __value) -> int:
        """
        Returns the number of elements with the specified value
        :param value: Any
        :return: int
        """
        return self.__list.count(__value)

    def extend(self, __iterable) -> None:
        """
        Add the elements of a list (or any iterable), to the end of the current list
        :param __iterable: list | tuple | set | ...
        :return: None
        """
        self.__check_types(__iterable)

        self.__list.extend(__iterable)

    def index(self, __value, __start: int = 0, __stop: int = maxsize) -> int:
        """
        Returns the index of the first element with the specified value
        :param __value: Any
        :param __start: int
        :param __stop: int
        :return: int
        :raise: ValueError if the value is not present
        """
        return self.__list.index(__value, __start, __stop)

    def insert(self, __index, __object) -> None:
        """
        Adds an element at the specified position
        :param __index: int
        :param __object: Any
        :return: None
        """
        self.__check_type(__object)

        self.__list.insert(__index, __object)

    def pop(self, __index: int = -1):
        """
        Removes the element at the specified position
        :param __index: int
        :return: item and index (default last)
        :raise: IndexError if list is empty or index is out of range.
        """
        return self.__list.pop(__index)

    def remove(self, __value) -> None:
        """
        Remove the first occurrence of x from the array.
        :param __value: Any
        :return: None
        """
        self.__list.remove(__value)

    def reverse(self) -> None:
        """
        Reverse the order of the items in the array.
        :return: None
        """
        self.__list.reverse()

    def sort(self, *, key: None = None, reverse: bool = False) -> None:
        """
        Sorts the list
        :param key: Callable
        :param reverse: bool
        :return: None
        """
        self.__list.sort(key=key, reverse=reverse)





