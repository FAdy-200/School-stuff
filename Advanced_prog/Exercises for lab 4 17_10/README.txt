Name: Fadi Alahmad Alomar		ID: 120180049

The code submitted is from my own creation

Exercise 1:
1. (d) Allows for objects of different types and behaviour to be treated as the same general type
2. (c) The program will have a more elegant design and will be easier to maintain and update
3. (c) Less restriction on the type values that can be passed to a given method
4. (a) 1 1 1
5. (b) 2
6. (d) B
7. (a) A non-private method in a superclass can be overridden


Exercise 2:

test case:
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


expected output:


Workshop - 12/03/2014 - Shutl

Students
1. Jane Doe - I am trying to learn programming and need some help
2. Lena Smith - I am really excited about learning to program!
Instructors
1. Vicky Python -  HTML, JavaScript
   I want to help people learn coding.
2. Nicole McMillan -  Ruby
   I have been programming for 5 years in Python and want to spread the love
