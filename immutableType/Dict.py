from typing import Any, Union, Type, final
from ._error import DictError, DictTypeValueError, DictTypeKeyError, DictKeyError
from .Subclass import notSubclass
from .List import List_

@notSubclass
@final
class Dict_:

    def __init__(self, dictionary: dict = {}, types: list[list[Type[Union[int, str, float, bool, tuple]]], Any] = None):
        """
        Create immutable dict type
        :param dictionary: a dict
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

    def __setitem__(self, key, value):
        self.set(key, value)
        return self

    def __bool__(self):
        return True if self.__dict else False

    def __len__(self):
        return len(self.__dict)

    def __iter__(self):
        return iter(self.__dict)

    def __eq__(self, other):
        return self.__dict == other

    def __and__(self, other):
        return self.__bool__() == other

    def __or__(self, other):
        return self.__bool__() != other

    def __str__(self):
        return str(self.__dict)

    def __add__(self, other: dict):
        """
        Add keys and values ti immutable dict
        :param other: a dict
        :return: Dict_
        """
        self.__check_type_value(other)
        self._check_types(other)
        for key, value in other.items():
            self.__dict[key] = value
        return self

    def __iadd__(self, other: dict):
        return self.__add__(other)

    def __sub__(self, other: list):
        """
        Remove keys in dict if the key is in "other"
        :param other: list of keys to remove
        :return: Dict_
        """
        other_ = List_(other)
        for key in other_:
            if key in self.__dict:
                del self.__dict[key]
        return self

    def __isub__(self, other: list):
        return self.__sub__(other)

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

    def __check_type_value(self, value):
        if not isinstance(value, (dict, Dict_)):
            raise DictError(value)

    @property
    def dict_(self) -> dict:
        """
        Return actual value
        :return: dict
        """
        return self.__dict

    @dict_.setter
    def dict_(self, new_dict):
        """
        Set a new value
        :param new_value: Any
        :return: None
        """
        self.__check_type_value(new_dict)
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

    def set(self, key: Any, value: Any) -> None:
        """
        Set a value in a nested dictionary.
        :param key: the key
        :param value: Any
        :return: None
        """
        self._check_types({key: value})
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