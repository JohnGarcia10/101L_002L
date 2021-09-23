#CS 101 Lab
#Program #2
#Jonathan Garcia Sanchez 
#jggfh@umsystem.edu
##
#Calculate the weight grade for Lab course depending on the grade in each category given
#1. start 
#2. assign an input for name of person who's grade is being calculated
#3. assign integer input for the grade of labs themselves
#4. make an if elif statement in case lab grade is over 100 to be 100 or less than 0 to be 0 
#5. reapt steps 3 and 4 for exam grade and attendance grade 
#6. calculate  weighted grade by multiplying lab grade by 0.7, exam by 0.2, and attendance by 0.1
#7. make if elif statement based on weight grade to determine what letter grade they have 
#8. end
print('*** Welcome to the LAB grade calculator! ***')
name = input('Who are we calculating grades for? ==>')
print() 
lab_grade = int(input('Enter the Labs grade? ==>'))
if lab_grade > 100:
    lab_grade = int(100)
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif lab_grade < 0:
    lab_grade = int(0)
    print('The lab value should be zero or greater.  It has been changed to zero')
print()
exam_grade = int(input('Enter the EXAMS grade? ==>'))
if exam_grade > 100:
    exam_grade = int(100)
    print('The exam value should have been 100 or less. It has been changed to 100')
elif exam_grade < 0:
    exam_grade = int(0)
    print('The lab value should be zero or greater.  It has been changed to zero')
print()
att_grade = int(input('Enter the attendance grade? ==>'))
if att_grade > 100:
    att_grade = int(100)
    print('The lab value should have been 100 or less. It has been changed to 100.')
elif att_grade < 0:
    att_grade = int(0)
    print('The lab value should be zero or greater.  It has been changed to zero')
print()

weight_grade = (lab_grade * 0.7) + (exam_grade * 0.2) + (att_grade * 0.1)
print('The weighted grade for', name, 'is', weight_grade)

if weight_grade >= 90:
    print(name, 'has a letter grade of A')
elif weight_grade >= 80:
    print(name, 'has a letter grade of B')
elif weight_grade >=70:
    print(name, 'has a letter grade of C')
elif weight_grade >= 60:
    print(name,'has a letter grade of D')
else:
    print(name,'has a letter grade of F')
print()
print('**** Thanks for  using the lab grade calculator ****')