# CSE314- Lab 4
#
# Topic: Object Oriented Concepts
# Author : Fadi Alahmad
# Date : 17/ 11/ 2020
# Exercise 1:
"""
1. (d) Allows for objects of different types and behaviour to be treated as the same general type
2. (c) The program will have a more elegant design and will be easier to maintain and update
3. (c) Less restriction on the type values that can be passed to a given method
4. (a) 1 1 1
5. (b) 2
6. (d) B
7. (a) A non-private method in a superclass can be overridden
"""


# Exercise 2:
class Members:
    """
    Members class to be a pareant class for all members
    """

    def __init__(self, name):
        self.name = name  # taking the name as an argument
        self.firstname = name.split()[0]  # splitting the name to first and last name
        self.lastname = name.split()[1]

    def introduce(self):
        """
        prints an introduction about the member
        """
        print(f"Hi, my name is {self.firstname}")


class Student(Members):
    """
    Student class that inherits the Members class
    """

    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason

    def get_reason(self):
        """
        :prints: the reason for attending
        """
        print(self.reason)


class Instructor(Members):
    """
    Instructor class that inherits the Members class with the added function add_skill
    """

    def __init__(self, name, bio):
        super().__init__(name)
        self.bio = bio
        self.skills = []

    def get_bio(self):
        print(self.bio)

    def add_skill(self, skill):
        """
        this function adds a skill to the instructor skill set
        :param skill: str
        :return:
        """
        self.skills.append(skill)


class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, part):
        """
        this function adds a participant to the workshop in its right place by checking its type and raising an error
        if the type is unknown
        :param part: Student or Instructor
        :return:
        """
        if type(part) == Student:
            self.students.append(part)
        elif type(part) == Instructor:
            self.instructors.append(part)
        else:
            raise Exception("Unknown participant type")

    def print_details(self):
        """
        this function prints the details of the workshop in an organized way
        :return:
        """
        print(f"Workshop - {self.date} - {self.subject}\n")
        print("Students")
        for i in range(len(self.students)):
            print(f"{i + 1}. {self.students[i].name} - {self.students[i].reason}")
        print("Instructors")
        for i in range(len(self.instructors)):
            print(f"{i + 1}. {self.instructors[i].name} - ", ", ".join(self.instructors[i].skills))
            print(f"   {self.instructors[i].bio}")


# TEST

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Ruby")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
