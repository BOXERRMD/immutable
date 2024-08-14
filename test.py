from immutableType import *

myDict2 = Dict_({'key2': Dict_({'key3': {}})})

myDict2.set(['key2', 'key3'], Str_("hello"))

'''print(myDict2.dict_)


print(myDict2.dict_)
print(myDict2.dict_['key2'].dict_)
print(myDict2.dict_['key2'].dict_['key3'])'''

print(myDict2.dict_)
print(myDict2.dict_.key2.dict_)
print(myDict2.dict_.key2.dict_.key3)

#myDict2.dict_['key2'] = 3



