from ._error import StrError
class Str_:
    def __init__(self, string: str) -> None:

        if not isinstance(string, str):
            raise StrError(string)

        self.__string = string

    @property
    def str_(self) -> str:
        return self.__string

    @str_.setter
    def str_(self, new_value):
        if not isinstance(new_value, str):
            raise StrError(new_value)

        self.__string = new_value

    def __str__(self):
        return self.__string

    def __repr__(self):
        return f"Str({self.__string!r})"