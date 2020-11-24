import Advanced_prog.Exercises_for_lab_5.Singlton as sing
class log(sing.Singlton):

    def __init__(self):
        cc = open("log.txt", "w")
        self.file = cc

    def Critical(self):
        print("Critical error")
        self.file.write("Critical error \n")

    def Error(self):
        print("Error")
        self.file.write("Error \n")
    def Warning(self,s):
        print("Warning"+s)
        self.file.write("Warning"+ s +"\n")
    def Info(self):
        print("Info")

    def Debug(self):
        print("Critical error")

    def pr(self, er):
        if er == ZeroDivisionError:
            self.Critical()
        elif er == TypeError:
            self.Error()
        elif er == "Adding Strings":
            self.Warning()
        # elif
