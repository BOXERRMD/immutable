from ._error import SubClassError

def notSubclass(cls):
    """
    Decorator for class

    Discard subclass.
    :raise SubClassError:
    """
    def init_subclass(cls, *args, **kwargs):
        raise SubClassError(cls)

    cls.__init_subclass__ = classmethod(init_subclass)
    return cls


