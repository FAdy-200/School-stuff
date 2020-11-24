import Advanced_prog.Exercises_for_lab_5.Singlton_Template as sing


class log(sing.Singlton):
    """
    the log class inherits the functions of the singlton class in the Singlton_template file
    """
    def __init__(self):
        """
        opens the file log.txt
        """
        cc = open("log.txt", "a")
        self.file = cc

    def Critical(self):
        print("Critical error")  # prints to the user the log
        self.file.write("Critical error \n")  # adds Critical error to the log file

    def Error(self):
        print("Error")  # prints to the user the log
        self.file.write("Error \n")  # adds Error to the log file

    def Warning(self, s):
        print("Warning " + s)  # prints to the user the log
        self.file.write("Warning " + s + "\n")  # adds Warning + the warning message passed by the function

    def Info(self, s):
        print("Info " + s)  # prints to the user the log
        self.file.write("Info " + s + "\n")   # adds Info + the passed info to the log file

    def Debug(self):
        print("Debug")  # prints to the user the log
        self.file.write("Debug\n")  # adds Debug to the log file

    def pr(self, er):
        """
        this function takes a param e and directs the call to the corresponding function
        :param er: Exception or str
        :return:
        """
        if er == ZeroDivisionError:
            self.Critical()
        elif er == TypeError:
            self.Error()
        elif er == "Adding Strings":
            self.Warning("Adding Strings")
        elif er == "Debug":
            self.Debug()
        else:
            self.Info(er)





