from ._error import BoolError
class Bool_:

    def __init__(self, boolean: bool) -> None:

        if not isinstance(boolean, bool):
            raise BoolError(boolean)

        self.__boolean = boolean

    @property
    def bool_(self) -> bool:
        return self.__boolean

    @bool_.setter
    def bool_(self, new_value):
        if not isinstance(new_value, bool):
            raise BoolError(new_value)

        self.__boolean = new_value

    def __str__(self):
        return self.__boolean

    def __bool__(self):
        return self.__boolean

    def __repr__(self):
        return f"Bool({self.__boolean!r})"