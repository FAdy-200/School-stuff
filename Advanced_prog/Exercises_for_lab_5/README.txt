Name: Fadi Alahmad Alomar		ID: 120180049

The code submitted is from my own creation

in the file named testing there is different test cases to go through all the functions of the file
logger.
in testing i try to create another instance of the class logger before every test to see if it is still following
singlton design pattern or not.


the expected output is as follows:

<<Advanced_prog.Exercises_for_lab_5.logger.log object at 0x00000272B3CCA3A0>
Critical error
<Advanced_prog.Exercises_for_lab_5.logger.log object at 0x00000272B3CCA3A0>
Error
<Advanced_prog.Exercises_for_lab_5.logger.log object at 0x00000272B3CCA3A0>
Warning Adding Strings
<Advanced_prog.Exercises_for_lab_5.logger.log object at 0x00000272B3CCA3A0>
Debug
<Advanced_prog.Exercises_for_lab_5.logger.log object at 0x00000272B3CCA3A0>
Info Info


and in the file log.txt it should contain:

Critical error
Error
Warning Adding Strings
Debug
Info Info
