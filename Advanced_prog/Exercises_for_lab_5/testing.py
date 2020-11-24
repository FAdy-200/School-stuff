import Advanced_prog.Exercises_for_lab_5.logger as log

l = log.log()
print(l)
# testing Critical Error as Division By zero
try:
    5 / 0
except Exception as e:
    l.pr(type(e))

l = log.log()
print(l)
# testing error as  type error
try:
    5 + "s"
except Exception as e:
    l.pr(type(e))

l = log.log()
print(l)
# Testing Warning as Adding strings
x = "x"
y = "y"
if type(x) == type(y) == str:
    l.pr("Adding Strings")

l = log.log()
print(l)
# testing Debug
l.pr("Debug")
l = log.log()
print(l)
# tesing Info
l.pr("Info")


