import Advanced_prog.Exercises_for_lab_5.logger as log

l = log.log()
print(l)
try:
    5/0
except Exception as e:
    print(type(e))
    l.pr(type(e))


l = log.log()
try:
    5+"s"
except Exception as e:
    print(type(e))
    l.pr(type(e))


l = log.log()
print(l)
# try:
#
# except Exception as e:
#     l.log.pr(type(e))
