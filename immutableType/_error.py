class NotMutableTypeError(Exception):
    pass


class StrError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a string, got {type(value).__name__}")

class IntError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a integer, got {type(value).__name__}")

class BoolError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a boolean, got {type(value).__name__}")

class TupleError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a tuple, got {type(value).__name__}")

class ListError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a list, got {type(value).__name__}")

class ListTypeError(NotMutableTypeError):

    def __init__(self, types, default_value, new_value) -> None:
        super().__init__(f"Expected {', '.join([i.__name__ for i in types if i != None])} types in {default_value}, not {type(new_value).__name__}")

class DictError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"Expected a dict, got {type(value).__name__}")

class DictTypeError(NotMutableTypeError):

    def __init__(self, types, default_value, new_value) -> None:
        super().__init__(f"Expected {', '.join([i.__name__ for i in types if i != None])} types in {default_value}, not {type(new_value).__name__}")

class DictTypeKeyError(NotMutableTypeError):

    def __init__(self, types, default_value, new_value) -> None:
        super().__init__(f"Expected {', '.join([i.__name__ for i in types if i != None])} key types in {default_value}, not {type(new_value).__name__}")

class DictTypeValueError(NotMutableTypeError):

    def __init__(self, types, default_value, new_value) -> None:
        super().__init__(f"Expected {', '.join([i.__name__ for i in types if i != None])} value types in {default_value}, not {type(new_value).__name__}")

class DictKeyError(NotMutableTypeError):

    def __init__(self, value) -> None:
        super().__init__(f"KeyError : {value}")