


class auto_instantiate(object):
    def __init__(self, fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return None

        value = self.fget(obj)
        setattr(obj, self.func_name, value)

        return value
