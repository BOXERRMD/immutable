Il est possible de :

- Rendre les variables immuable
- Forcer un type dans une fonction (ne pas accepter d'autres types)

```python
from immutableType import *

def test(coucou = None):
    coucou.list_ = [True, None]
    print(coucou)

#permet de forcer le type bool dans le paramètre "coucou". "_list" n'est pas obligatoire
test(List_(_list=[],types=[bool]))
```