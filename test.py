from immutableType import *

a = Dict_({'a': 1, 'b':2, 'c':3})

for key, value in a.items():
    print(key, value)

a['a'] = 10.0