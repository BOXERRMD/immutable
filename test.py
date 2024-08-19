from immutableType import *

myDict2 = Dict_({'key2': Dict_({'key3': 'value3'})})

print(myDict2.dict_['key2']) # print : <immutableType.Dict.Dict_ object at ...>

myDict2.set(['key2', 'key3'], 'coucou')
print(myDict2.dict_['key2'].dict_)

#myDict2.dict_['key2'] = 3



