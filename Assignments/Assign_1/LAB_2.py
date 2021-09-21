print('*** Welcome to the LAB grade calculator! ***')
name = input('Who are we calculating grades for? ==>')
print() 
lab_grade = int(input('Enter the Labs grade? ==>'))
if lab_grade > 100:
    lab_grade = int(100)
    print('The lab value should have been 100 or less. It has been changed to 100.')
print()
exam_grade = int(input('Enter the EXAMS grade? ==>'))
if exam_grade < 0:
    exam_grade = int(0)
    print('The exame value should habe been zero or greater. It has been changed to zero')
print()
att_grade = int(input('Enter the attendance grade? ==>'))

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