from typing import Any, Union, Type
from ._error import DictError, DictTypeValueError, DictTypeKeyError, DictKeyError

class Dict_:

    def __init__(self, dictionary: dict = {}, types: list[list[Type[Union[int, str, float, bool, tuple]]], Any] = None):
        """
        Setup a dictionary and types.
        :param dictionary: dict
        :param types: list[list[type key], type values]
        """

        self.__types = types

        if not isinstance(dictionary, dict):
            raise DictError(dictionary)

        self.__dict = dictionary
        self._check_types(dictionary)
        self.__dict = AttributDict(dictionary)


    def __getitem__(self, item):
        return self.__dict[item]

    def __bool__(self):
        return True if self.__dict else False

    def __len__(self):
        return len(self.__dict)

    def __iter__(self):
        return iter(self.__dict)


    def _check_types(self, value: dict) -> None:
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

        self._check_types(new_dict)

        self.__dict = new_dict


    def get(self, keys: Union[list[Union[str, int, tuple, float, bool]]]) -> Any:
        """
        Get the value from a key
        :param key: str | int | float
        :return: Any
        """
        d = self.__dict

        for i in keys:

            if isinstance(d, Dict_):

                if i not in d.dict_.keys():
                    raise DictKeyError(i)

                d = d.dict_[i]

            else:
                if i not in d.keys():
                    raise DictKeyError(i)

                d = d[i]

        return d

    def set(self, keys: list[Union[str, int, tuple, float, bool]], value: Any) -> None:
        """
        Set a value in a nested dictionary using a list of keys.
        :param key: list of keys (str | int | float) representing the path in the nested dictionary
        :param value: Any
        :return: None
        """
        d = self.__dict

        for i in keys[:-1]:
            if isinstance(d, Dict_):
                # Vérifiez les types dans Dict_

                # Si la clé n'existe pas, créer un nouveau Dict_
                if i not in d.dict_.keys():
                    d.dict_[i] = Dict_({})

                d._check_types(d.dict_)
                # Descendre d'un niveau dans le dictionnaire
                d = d.dict_[i]

            else:
                # Pour les dictionnaires standards
                if i not in d:
                    d[i] = {}
                d = d[i]  # Descendre d'un niveau dans le dictionnaire


        # Assigner la valeur à la clé finale
        if isinstance(d, Dict_):
            d._check_types({keys[-1]: value})
            d.dict_[keys[-1]] = value
        else:
            d[keys[-1]] = value



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