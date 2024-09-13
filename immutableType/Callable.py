from .List import List_
from .Dict import Dict_
from typing import Callable, Any, Type
from ._error import CallableError, CallableTypeError, CallableKwargsKeyError, CallableKwargsValueTypeError
from inspect import getmembers, signature


class Callable_:

    def __init__(self, _callable: Callable, args_types: list[Type] = [], kwargs_types: dict[str | Type] = {}):
        """
        Define a immutable object from a callable to setup immutable params in callable.
        :param _callable: Callable (func, class)
        :param params_type: list[Any] -> reload into a immutable List_
        """

        if not callable(_callable):
            raise CallableError(_callable)

        # if not args types configured


        self.__callable = _callable
        self.__args_types = List_(args_types)
        self.__kwargs_types = Dict_(kwargs_types)


    def call(self, *args, **kwargs) -> Any:
        """
        Check all params and call the function
        :param args:
        :param kwargs:
        :return: Any
        :raises CallableTypeError, CallableKwargsKeyError, CallableKwargsValueTypeError: ``CallableTypeError`` -> positional type argument not found in **[[HERE], {...}]** ``CallableKwargsKeyError`` -> Key not found **[[...], {'HERE': ...]]** ``CallableKwargsValueTypeError`` -> Type value not found **[[...], {'...': [HERE]}]**
        """

        self.__check_args(args)
        self.__check_kwargs(kwargs)

        return self.__callable(*args, **kwargs)


    def __check_args(self, args: tuple) -> None:
        """

        :param args: all positional arguments in [['TEST', 1, True], {...}][0]
        :return: None
        """

        for i in range(len(args)):

            if type(args[i]) not in self.__args_types.list_:

                raise CallableTypeError(self.__args_types.list_, self.__callable.__name__, args[i], i)




    def __check_kwargs(self, kwargs: dict) -> None:
        """
        Check all kwargs type argument in [[...], {'NAME': type}][1]
        :param kwargs: All positional arguments
        :return: None
        """
        kwargs_types = self.__kwargs_types.dict_

        for key, value in kwargs.items():
            if key not in kwargs_types.keys():
                raise CallableKwargsKeyError(key, [i for i in kwargs_types.keys()])

            if type(value) not in kwargs_types[key]:
                raise CallableKwargsValueTypeError(kwargs_types[key], value, key, self.__callable)