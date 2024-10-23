# Immutable-Python-type
_package for make immutable all types in Python_

### Support types and replaced by:

- int = ``Int_()``
- str = ``Str_()``
- bool = ``Bool_()``
- set = ``Set_()``
- tuple = ``Tuple_()``
- list = ``List_()``
- dict = ``Dict_()``

### Examples

```python
from immutableType import Bool_, Int_

immutable_bool = Bool_(True) # init immutable boolean
immutable_int = Int_(1) # init immutable integer

immutable_bool.bool_ = 1234 # raise an error
immutable_bool.bool_ = False # good

print(immutable_int == immutable_bool) # print False
"""
Immutable boolean consider True = 1 and False = 0
"""
```

### ``Int_(integer: int)``
```python
from immutableType import Int_

my_int = Int_(1234) # init immutable integer
my_int.int_ # property to get the value in 'int' type
```
> ``Int_()`` have methods :
> - ``__str__`` : return string with the integer value
> - ``__int__`` : return the integer value
> - ``__bool__`` : return **True** if the **value == 1** else **False**
> - ``__eq__, __and__, __or__, __iand, __ior__`` : basic comparaison
> - ``__add__, __sub__, __iadd__, __isub__, __mul__, __imul__, __truediv__, __itruediv__, __pow__, __ipow__`` : basic operation

_redaction in progress..._
