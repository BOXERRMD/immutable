from ._error import IntError
class Int_:
    def __init__(self, integer: int) -> None:

        if not isinstance(integer, int):
            raise IntError(integer)

        self.__integer = integer

    @property
    def int_(self) -> int:
        return self.__integer

    @int_.setter
    def int_(self, new_value):
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