from .Str import Str_
from .Int import Int_
from .Bool import Bool_
from .Tuple import Tuple_
from .List import List_
from .Dict import Dict_
from typing import Callable, Any


class Convert:
    def __init__(self, value: Any):
        """
        Convert all types to immutable
        :param value: Any
        """
        self.result = self.__make_immutable(value)

    def __make_immutable(self, value):

        if isinstance(value, dict):
            # Si la valeur est un dictionnaire, convertir ses clés et valeurs en immuables
            return Dict_(dictionary={k: self.__make_immutable(v) for k, v in value.items()})

        elif isinstance(value, list):
            # Si la valeur est une liste, convertir chaque élément en immuable
            return List_(_list=[self.__make_immutable(v) for v in value])

        elif isinstance(value, tuple):
            # Si la valeur est un tuple, convertir chaque élément en immuable
            return Tuple_((self.__make_immutable(v) for v in value))

        elif isinstance(value, int):
            # Si la valeur est un integer, convertir l'élément en immuable
            return Int_(value)

        elif isinstance(value, str):
            # Si la valeur est un string, convertir l'élément en immuable
            return Str_(value)

        elif isinstance(value, bool):
            # Si la valeur est un boolean, convertir l'élément en immuable
            return Bool_(value)


        else:
            # Si la valeur est un type de base (int, str, float, etc.), on la laisse telle quelle
            return value

    def get(self) -> Callable:
        """
        Get all types immutable
        :return: Callable
        """
        return self.result







