class Singlton:
    """
    Singlton class to create only one instance of the class that inherits from it
    """
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = cls.instance = super (Singlton, cls).__new__(cls)
        return cls.instance
