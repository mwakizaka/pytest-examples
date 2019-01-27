class Operator(object):
    _instance = None
    var_x = "X"
    var_y = "Y"
    var_Z = "Z"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            print("Starry night knows how I feel")
        return cls._instance
