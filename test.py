from immutableType import *

myDict2 = Dict_(types=[[str, int], str, Dict_], dictionary={'key2': Dict_({'key3': 'value3'}, types=[[str], str, Dict_])})

print(myDict2.dict_['key2']) # print : <immutableType.Dict.Dict_ object at ...>

myDict2.set(['key2', 3], 'coucou')
print(myDict2.dict_['key2'].dict_)

#myDict2.dict_['key2'] = 3



