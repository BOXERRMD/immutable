from immutableType import *

def test(arg1: int, arg2: int):

    print(arg1 + arg2)


Callable_(test, args_types=[int, str]).call(1, 5)
