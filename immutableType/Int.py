class Int_:
    def __init__(self, integer: int) -> None:

        if not isinstance(integer, int):
            raise TypeError(f"Expected a integer, got {type(integer).__name__}")

        self.__integer = integer

    @property
    def int_(self) -> int:
        return self.__integer

    @int_.setter
    def int_(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError(f"Expected a integer, got {type(new_value).__name__}")
        self.__integer = new_value

    def __str__(self):
        return str(self.__integer)

    def __int__(self):
        return self.__integer

    def __repr__(self):
        return f"Int({self.__integer!r})"