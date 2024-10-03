from immutableType import *

@callable_(args_types=[int], kwargs_types={'b': [str]})
def test(a: int, b='x'):

    for i in range(a):
        b += b
    return b

print(test(3, b='abc'))


