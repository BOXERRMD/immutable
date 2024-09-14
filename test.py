from immutableType import *


@callable_(args_types=[List_])
def test(l: List_):

    return l[1]


print(len(Dict_({'coucou': 1, 2: 5})))