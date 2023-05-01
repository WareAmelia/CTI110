   # CTI-110

   # P4HW1 - Score List

   # Amelia Ware

   # Date

   #

#assign variables
grade = 0
num_grade = int(input('How many grades would you like to enter? '))
total_grade = 0
new_grade = 0
grade_num = 0
grades = []
letter = '0'

#determine the range
for number in range(0, num_grade):
    new_grade= int(input('What was your score: '))
    if 0<=new_grade<=100:
        grade+=new_grade
    else:
      #tell them if there number is wrong
         print('Invalid grade.\nGrade should be between 0 and 100')
         new_grade = int(input('Enter new grade: '))
    grades.append(new_grade)


if new_grade >= 0 and new_grade <= 100:
 
  #avg the grades
    avg_grade = grade/num_grade
  #fail at telling them their grade is invalid
else:
   print('Please recaculate your grades.')
#determine letter
if 90<=avg_grade <= 100:
    letter = 'A'
elif 80<= avg_grade <=89:
    letter = 'B'
elif 70<= avg_grade <=79:
    letter = 'C'
elif 60<= avg_grade <=69:
    letter = 'D'
elif 0<= avg_grade <=59:
    letter = 'F'
  #print all of the data
print('Lowest: ', min(grades))
grades.remove(min(grades))
print('New list: ', (grades))
print(letter)