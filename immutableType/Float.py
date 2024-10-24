from ._error import FloatError
from typing import final
from .Subclass import notSubclass

@final
@notSubclass
class Float_:

    def __init__(self, _float: float) -> None:
        """
        Create immutable float type
        :param integer: a float
        """

        self.__check_type(_float)

        self.__float = _float

    def __str__(self):
        return str(self.__float)

    def __int__(self):
        return self.__float

    def __bool__(self):
        return True if self.__float == 1.0 else False

    def __repr__(self):
        return f"Int({self.__float!r})"

    def __eq__(self, other):
        return self.__float == other

    def __and__(self, other):
        return self.__bool__() & other

    def __iand__(self, other):
        self.__float &= other
        return self

    def __or__(self, other):
        return self.__bool__() | other

    def __ior__(self, other):
        self.__float |= other
        return self

    def __add__(self, other):
        self.__check_type(other)
        self.__float += other
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.__check_type(other)
        self.__float -= other
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        self.__float *= other
        return self

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        self.__float = self.__float / other
        return self

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __mod__(self, other):
        self.__float %= other
        return self

    def __imod__(self, other):
        return self.__mod__(other)

    def __pow__(self, power, modulo=None):
        self.__check_type(power)
        self.__float **= power
        return self

    def __ipow__(self, other):
        return self.__pow__(other)


    def __check_type(self, value):
        if not isinstance(value, float):
            raise FloatError(value)

    @property
    def float_(self) -> float:
        """
        Return actual value
        :return: int
        """
        return self.__float

    @float_.setter
    def float_(self, new_value):
        """
        Set a new value
        :param new_value: an integer
        :return: None
        """
        self.__check_type(new_value)
        self.__float = new_value
