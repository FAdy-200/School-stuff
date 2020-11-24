# import Advanced_prog.Exercises_for_lab_5.logger as log


class Singlton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = cls.instance = super (Singlton, cls).__new__(cls)
        return cls.instance
