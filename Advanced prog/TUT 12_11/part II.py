class Error(Exception):
    pass


class UsernameError(Error):
    def __str__(self):
        return "User already exists"


class AgeError(Error):
    def __str__(self):
        return "Age is bellow 16"


class EmailError(Error):
    def __str__(self):
        return "invalid email"


class User:
    dic = {}

    def __init__(self, name, age, email, dic=dic):
        self.name = name
        self.age = age
        self.email = email
        try:
            if self.age < 16:
                raise AgeError
            if self.name in dic.keys():
                raise UsernameError
            if "@" not in self.email or "." not in self.email:
                raise EmailError
        except Exception as e:
            print(e)
        dic[self.name] = (self.age, self.email)


u1 = User("fady", 16, "asdasd@asd.asd")
u2 = User("fady", 16, "asdasd@asdsd")
