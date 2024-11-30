from .Str import Str_
from .Int import Int_
from .Bool import Bool_
from .Tuple import Tuple_
from .List import List_
from .Dict import Dict_
from .Set import Set_
from typing import Callable, Any


class Convert:
    def __init__(self, value: Any):
        """
        Convert ALL variables to immutable types.
        :param value: Any
        """
        self.__result = self.__make_immutable(value)

    def __make_immutable(self, value):

        if isinstance(value, dict):
            # Si la valeur est un dictionnaire, convertir ses clés et valeurs en immuables
            return Dict_(dictionary={k: self.__make_immutable(v) for k, v in value.items()})

        elif isinstance(value, list):
            # Si la valeur est une liste, convertir chaque élément en immuable
            return List_(_list=[self.__make_immutable(v) for v in value])

        elif isinstance(value, tuple):
            # Si la valeur est un tuple, convertir chaque élément en immuable
            return Tuple_(tuple([self.__make_immutable(v) for v in value]))

        elif isinstance(value, int):
            # Si la valeur est un integer, convertir l'élément en immuable
            return Int_(value)

        elif isinstance(value, str):
            # Si la valeur est un string, convertir l'élément en immuable
            return Str_(value)

        elif isinstance(value, bool):
            # Si la valeur est un boolean, convertir l'élément en immuable
            return Bool_(value)

        elif isinstance(value, set):
            #si la valeur est un set, convertir l'élément en immuable
            return Set_(value)

        else:
            #sinon retourne la valeur par défaut
            return value

    @property
    def get(self) -> Callable:
        """
        Get all types immutable
        :return: Callable
        """
        return self.__result



def convert_(is_class=False):
    """
    Decorator for convert parameters type

    Convert all parameters passed in function to immutable type.
    :param is_class: If used on function in class
    :return: None
    """
    def wrapper(func):
        def convert_all_types(*args, **kwargs):

            if is_class:
                args = args[1:]

            args = Convert(args).get
            kwargs = Convert(kwargs).get
            func(*args, **kwargs.dict_)

        return convert_all_types
    return wrapper



