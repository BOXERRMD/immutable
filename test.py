from immutableType import *

myDict2 = Dict_({'key2': Dict_({'key3': {}})})

myDict2.set(['key2', 'ok'], Str_("hello"))


print(myDict2.get(['key2', 'ok']))

#myDict2.dict_['key2'] = 3



