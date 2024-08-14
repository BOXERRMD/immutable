from typing import Any
from ._error import DictError, DictTypeError, DictTypeValueError, DictTypeKeyError

class Dict_:

    def __init__(self, dictionary: dict = {}, types: list[list[type], type] = None):
        """
        Setup a dictionary and types.
        :param dictionary: dict
        :param types: list[list[type key], type values]
        """

        self.__types = types

        if not isinstance(dictionary, dict):
            raise DictError(dictionary)

        self.__dict = dictionary
        self.__check_types(dictionary)
        self.__dict = AttributDict(dictionary)



    def __check_types(self, value) -> None:
        """
        Check key and value type of "value" dictionary to self.types
        :param value: dict
        :return: None
        """
        if self.__types is None:
            self.__types = [[]]

            for key in value.keys():
                u = type(value[key])
                k = type(key)

                if k not in self.__types[0]: #Si le type de la clé n'est pas dans la liste de self.__types
                    self.__types[0].append(k)

                if u not in self.__types: #Si le type de la valeur n'est pas dans self.__types
                    self.__types.append(u)

            return

        for key, value_dic in value.items():

            k = type(key)
            vd = type(value_dic)

            if k not in self.__types[0]:
                e = DictTypeKeyError(self.__types[0], self.__dict, key)
                e.add_note(f"{k.__name__} is not an accepted key type")
                raise e

            if vd not in self.__types[1:]:
                e = DictTypeValueError(self.__types[1:], self.__dict, value_dic)
                e.add_note(f"{vd.__name__} is not an accepted value type")
                raise e


    @property
    def dict_(self):
        return self.__dict

    @dict_.setter
    def dict_(self, new_dict):
        if not isinstance(new_dict, dict):
            raise DictError(new_dict)

        self.__check_types(new_dict)

        self.__dict = new_dict


    def get(self, key: str | int | float) -> Any:
        """
        Get the value from a key
        :param key: str | int | float
        :return: Any
        """
        return self.__dict[key]


    def set(self, key: Any, value: Any) -> None:
        """
        Set à value from a key
        :param key: str | int | float
        :param value: Any
        :return: None
        """

        self.__check_types({key: value})

        self.__dict[key] = value




class AttributDict(dict):
    def __getattr__(self, key):
        if key in self:
            value = self[key]
            if isinstance(value, dict):
                return AttributDict(value)  # Convertir les sous-dictionnaires aussi
            return value
        raise AttributeError(f"'AttributDict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
        else:
            raise AttributeError(f"'AttributDict' object has no attribute '{key}'")