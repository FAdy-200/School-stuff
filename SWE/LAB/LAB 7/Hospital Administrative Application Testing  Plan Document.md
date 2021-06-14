# Hospital Administrative Application Testing Plan Document 

## TABLE OF CONTENT
- [](#)
  - [TABLE OF CONTENT](#table_of_content)
  - [IDENTIFICATION INFORMATION SECTION](#identification-information-section)
    - [PRODUCT](#product)
    - [PROJECT DESCRIPTION](#project-description)
    - [TEST PERSONNEL](#test-personnel)
    - [PROGRAMMERS](#programmers)
  - [UNIT TEST SECTION](#unit-test-section)
    - [UNIT TEST STRATEGY AND EXTENT OF UNIT TESTING:](#unit-test-strategy-and-extent-of-unit-testing)
  - [OUTSIDE VIEW TEST SECTION](#outside-view-test-section)
    - [OUTSIDE VIEW TEST STRATEGY AND EXTENT OF OUTSIDE VIEW TESTING](#outside-view-test-strategy-and-extent-of-outside-view-testing)
    - [OUTSIDE VIEW TEST CASES](#outside-view-test-cases)
      - [TEST CASE 1](#test-case-1)
      - [TEST CASE 2](#test-case-2)
      - [TEST CASE 3](#test-case-3)
      - [TEST CASE 4](#test-case-4)
      - [TEST CASE 5](#test-case-5)
    - [OUTSIDE VIEW SCORE](#outside-overall-score)

## IDENTIFICATION INFORMATION SECTION

### PRODUCT

- **Product Name:** Hospital Administrative Application

### PROJECT DESCRIPTION

Track  hospitals Intensive Care Units beds and ventilators occupancy in a given district. And show small statistics about them to the Health district manager

### TEST PERSONNEL

|Name|ID|
|:-:|:-:|
|Fadi Alahmad Alomar | 120180049
|Mazen Khodier  | 120180019
|Abdelrahman Medhat Saad|   120180025
|Martin ihab   |120180004

### PROGRAMMERS

- Ahmed Salman
- Menna tullah
- Omar Alaa
- Omar bahaa

## UNIT TEST SECTION

Testing modules against known input to see if they output what is expected from them and in the way it was intended by the programer.

### UNIT TEST STRATEGY AND EXTENT OF UNIT TESTING

Testing ```Stats``` module to see if it performs the way expected. Methods tested include:
- ```test_average_used_vents```
- ```test_average_used_beds```
- ```test_percentage_vents```
- ```test_percentage_beds```
- ```test_check_occupancy```

The file **_StatsUnitTesting.py_** is attached along this documentation and should be placed in the main root directory before being run.

Unfortunately, There were some dependencies between files and hardcoded variables (database file path) that rendered individual unit testing almost impossible to implement. Aside from that, only the ```test_average_used_beds``` methods showed unexpected behavior probably due to a different interpretation on the programmer's side.

## OUTSIDE VIEW TEST SECTION

Testing the entire software from the point of view of the user and the SOFTWARE REQUIREMENTS for it

### OUTSIDE VIEW TEST STRATEGY AND EXTENT OF OUTSIDE VIEW TESTING

Only test the outer view and the results.

### OUTSIDE VIEW TEST CASES

| \#  | OBJECTIVE  | EXPECTED RESULTS |
| --- | ---------  | ---------------- |
| 1   | Test the software from the Hospital Manager point of view  with the right data format entered  | Success message |
| 2   | Test the software from the Hospital Manager point of view with the wrong data format entered   | Fail\Try again message || 3   | Test the software from the Hospital Manager point of view with the wrong data format entered   | Fail\Try again message |
| 3   | Test the software from the Hospital Manager point of view with the empty fields  | Fail\Try again message |
| 4   | Test the software from the District Manager point of view without a warning| UI showing the right stats of the hospitals |
| 5   | Test the software from the District Manager point of view  with a warning | UI showing the right stats of the hospitals  and a warning message  about reaching a cortical state in the numbers of beds or ventilators |

#### TEST CASE 1

| step \#  | DETAILS | INPUT | EXPECTED RESULTS | AS EXPECTED  (T/F) |
| :---: | --------- | ----- | ---------------- |-----------|
|1|Run the command```python hospital_system -u manager```|NONE|GUI showing fields to enter all the needed input|T|
|2|Input the data each in its right place with the right format|Hospital ID = 1, # of Beds = 99,# of Ventilators = 90, # max bed = 40,#max Ventilators = 40, Date = 2021-04-16|Window showing the process  has been done successfully |T|

#### TEST CASE 2

| step \#  | DETAILS | INPUT | EXPECTED RESULTS | AS EXPECTED (T/F) |
| :---: | --------- | ----- | ---------------- |-----------|
|1|Run the command```python hospital_system -u manager```|NONE|GUI showing fields to enter all the needed input|T|
|2|Input the data each in its right place with the right format|Hospital ID = 3.3, # of Beds = 99,# of Ventilators = 5.5, # max bed = T,#max Ventilators = 6000, Date = 2021-06-11|Window showing there was an error in the entered data  |F|

#### TEST CASE 3

| step \#  | DETAILS | INPUT | EXPECTED RESULTS | AS EXPECTED (T/F) |
| :---: | --------- | ----- | ---------------- |-----------|
|1|Run the command```python hospital_system -u manager```|NONE|GUI showing fields to enter all the needed input|T|
|2|Input the data each in its right place with the right format| NONE |Window showing there was  an empty field in the entered data  |T|

#### TEST CASE 4

| step \#  | DETAILS | INPUT | EXPECTED RESULTS | AS EXPECTED  (T/F) |
| :---: | --------- | ----- | ---------------- |-----------|
|1|Run the command```python hospital_system -u manager```|NONE|GUI showing fields to enter all the needed input|T|
|2|Input the data each in its right place with the right format|Hospital ID = 1, # of Beds = 99,# of Ventilators = 90, # max bed = 40,#max Ventilators = 40, Date = 2021-06-10|Window showing the process  has been done successfully |T|
|3|Run the command```python hospital_system -u official```|NONE|GUI showing Summary of the hospitals statistics without a capacity warning|T|

#### TEST CASE 5

| step \#  | DETAILS | INPUT | EXPECTED RESULTS | AS EXPECTED  (T/F) |
| :---: | --------- | ----- | ---------------- |-----------|
|1|Run the command```python hospital_system -u manager```|NONE|GUI showing fields to enter all the needed input|T|
|2|Input the data each in its right place with the right format|Hospital ID = 1, # of Beds = 90,# of Ventilators = 90, # max bed = 90,#max Ventilators = 90, Date = 2021-06-10|Window showing the process  has been done successfully |T|
|3|Run the command```python hospital_system -u official```|NONE|GUI showing Summary of the hospitals statistics with a capacity warning|T|

#### OUTSIDE OVERALL SCORE

|Test case #|PASS/FAIL|
|:--:|:--:|
|1|PASS|
|2|FAIL|
|3|PASS|
|4|PASS|
|5|PASS|