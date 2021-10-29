#CS101 Week   9
#Program  Lab week 9
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
# Problem: Calculate the min, max, average, and standard deviation of weighted grades depending on inputs from the user about  their test or programs to figure out what the weighted score is. Allow for add or remove of test and assignemtns 
#1. start 
#2. set up two empty list for test and assignments, then  have test w variable equal to 0.y and assignment weight variable equal to 0.4
#3. set up menu function that has all choice user has
#4. set up funciton to get grades that takes a string, while true loop for grades equal to float input, if the grades is less than 0 set ask again then brek return grades
#5. remove grade function takes grades and string as  parameter set grade equal to the get grades function, if grade is not in grades print that they could not remove. else remove grade
#6. set up function for standard devation inside have a forumla way to find the std return it
#7. set up function to show grades, and if it 0 set it to have  n/a
#8. else solve for average, minumum , maximum, and standard  deviation using the function for it, then output it on on a line 
#9. set up a  average  function that takes grades as parameter if lengeth is 0 then return 0 and if not return the sum of grades divied by the length 
#10. have a results function that takes the list as parameters set two varaibles to be the average for test and assignments using the average function 
#11. print out the table that shows what each number means on the table
#12. then use show grades functions to also show the test and assignments with what was previously used
#13. calcuate for the weight and print it
#14. in the main have a while true with menu function then ask user for a choice, set if elif depending on the choices from the menu and dpending on each one attached the functions used, if Q quit


test = []
assignments = []
test_w = 0.6
assignment_w = 0.4


def menu():
    print('Grade Menu')
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Test')
    print('4 - Add Assignment')
    print('5 - Remove Assigment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()

def get_grades(string1):
    while True:
        try:
            grades = float(input(string1))
            if grades < 0:
                grades = float(input(string1))
            break
        except ValueError:
            pass 
    return grades

def remove_grade(grades,string1):
    grade = get_grades(string1)
    if grade not in grades:
        print('Could not find that score to remove')
    else:
        grades.remove(grade)

def std(grades,avg):
    sq = 0 
    for grade in grades:
        sq += (avg - grade) ** 2
    return (sq / len(grades)) ** 0.5

def show_grades(grades,string1):
    if len(grades) == 0:
        print('{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}'.format(string1, '0','n/a','n/a','n/a','n/a'))
    else:
        avg = sum(grades) / len(grades)
        std1 = std(grades,avg)
        maximum = max(grades)
        minimum = min(grades)
        print("{:<10} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f}".format(string1, len(grades), minimum, maximum, avg , std1))

def avg1(grades):
    if len(grades) == 0:
        return 0
    else:
        return sum(grades) / len(grades)

def results(test,assignments):
    avg_a = avg1(test)
    avg_t = avg1(assignments)
    print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format( "Type", "#", "min", "max", "avg", "std"))
    print('='*70)
    show_grades(test,'Test')
    show_grades(assignments,'Programs')
    weight = avg_t * test_w + avg_a * assignment_w
    print('The weight score is {}'.format(round(weight,2)))


while True:
    menu()
    choice = input('==> ').upper()
    if choice == '1':
        grade = get_grades('\nEnter the new Test score 0-100 ==> ')
        test.append(grade)
    elif choice == '2':
        remove_grade(test,'\nEnter the new Test to remove 0-100 ==> ')
    elif choice == '3':
        test.clear()
    elif choice == '4':
        grade = get_grades('\nEnter the new Assignment score 0-100 ==> ')
        assignments.append(grade)
    elif choice == '5':
        remove_grade(assignments,'\nEnter the Assignment to remove 0-100 ==> ')
    elif choice == '6':
        assignments.clear()
    elif choice == 'D'.upper():
        results(test,assignments)
    elif choice == 'Q':
        break