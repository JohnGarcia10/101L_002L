#CS101 Lab 6
#Program Lab 6 
#Jonathan Garcia  Sanchez
#jggfh@umsystem.edu
#PROBLEM: ask user for a library card number and find out if it is a valid card number then find out what school they are from and grade. If the card is invalid tell the user the reason why and try again until they input a correct amount
########

#1. start 
#2. Begin with first functions being get school that takes library card as a parameter
#3. Inside need  if elif statements, first if is if card index 5 is equal to 1 then return School of Computing and Engineering
#4. next elif if card index 5 is equal to 2 return School of law, another elif if card index 5 is equal to 3 return college of arts and sciences 
#5. else return invalid  school
#6. Set up next fucntion to be get grade that takes same card parameter
#7. get grade will have multiple if elif statemts, the first is if card index 6 is equal to 1 return freshman 
#8. elif card index 6 is equal  to 2 return sophmore, another eilf for idex 6 being equal to 3 return junior, and if it is 4 return senior
#9. anyting else return invalid grade
#10. Another function for character value that takes a singe string character 
#11. have a variable equal to ord of the singel string character, x for example
#12. have an if elif statement for if that variable is greater than or equal to 65 and less than or equal to 90 then return that variable - 65
#13. elif the variable is greater than or equal to 48 and less than or equal to 57 return the variable - 48
#14. Next function set up to check digit with card number as parameter, inside set a total to 0 then begin a  for loop for i in range of card num length 
#15. inside the loop set digit equal to character value  (fucntion) with the parameter card[i]
#16. Then set total equal to total plus digit * (i+1), then return total mod(%) 10
#17. Begin new fucnciton for verify check digit with card number as parameter 
#18. if the card number lenght isn't equal to 10 print that it is invalid and must be 10 then return false
#19. then have a for loop for i in range of 5, inside have if statement for card number index i being less than 'A' or greater than 'Z'. Print it is invalid and that the first 5 characters must be a-z and tha the invalid character is at string(i) and card number index i
#20. outside of that for loop start another for loop for i in ragne of 7, 10. inside have an if the card number index i is less than '0' or greater than '9'. Print invalid and print the last 3 character must be 0-9 with same print as previous of where the card number is wrong. Return False
#21. outside of  that loop have if statement if card index 5 does not equal '1' and does not equal '2' and doe4s not equal '3'. Print invalid and print the sixth chracter must be 1 2  or 3
#22. another if for the card's six indes not being equal to '1', not equal to '2', not equal to '3', and not equal to '4'. Print invalid and print the seventh caracter must be 1 2 3 or 4 then return false
#23. have check digit variable  equal to get check digit with card number as parameter 
#24. have a value varieble equal to int card number at the 9th index, then have an if statement for the value not equal to check digit. Indise print that hte check digit does not match the calcualted value at the check digit and value, then return false
#25. else print that the library card is valid then return true
#26. now have an if  name equal main for the rest of the program
#27. set string equal to 'Linda Hall'
#28. Set new string to string cetner 48
#29. have string 2 equal to 'Library Card Check'
#30. then have new string2 equal to string2.center48
#31. print new string, print new string2 and then print '=' * 48
#32. then have a while true loop inside have card num variable that is used in the parameters of previous funcitons as input
#33. if card num equal ' ' break
#34. then have a verify variable equal to verfiy check digit fuction with card number as parameter
#35. If the verify variable equal true then print the card belongs to student in the get school fucntion 
#36. print the card belongs to the get grade function 
#37. Stop
#################################
##############


def get_school(card_num):
    if card_num[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif card_num[5] == '2':
        return 'School of Law'
    elif card_num[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid school'




def get_grade(card_num):
    if card_num[6] == '1':
        return 'Freshman'
    elif card_num[6] == '2':
        return 'Sophomore'
    elif card_num[6] == '3':
        return 'Junior'
    elif card_num[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'




def character_value(x):
    x_value = ord(x)
    if x_value >= 65 and x_value <= 90:
        return x_value - 65
    elif x_value >= 48 and x_value <= 57:
        return x_value - 48


def get_check_digit(card_num):
    total = 0
    for i in range(len(card_num)):
        digit = character_value(card_num[i])
        total = total + digit * (i+1)
    return total % 10


def verify_check_digit(card_num):
    if len(card_num) != 10:
        print('Library card is invalid.')
        print('The length of the number given must be 10')
        print()
        return False
    for i in range(5):
        if card_num[i] < 'A' or card_num[i] > 'Z':
            print('Library card is invalid')
            print('The first 5 characters must be A-Z, the invalid charcter is at',str(i),'is',card_num[i])
            print()
            return False
    for i in range(7,10):
        if card_num[i] < '0' or card_num[i] > '9':
            print('Library card is invalid')
            print('The last 3 characters must be 0-9, the invalid characters is at',str(i),'is',card_num[i])
            print()
            return False
    if card_num[5] != '1' and card_num[5] != '2' and card_num[5] != '3':
        print('Library card is invalid')
        print('The sixth character must be 1 2 or 3')
        return False
    if card_num[6] != '1' and card_num[6] != '2' and card_num[6] != '3' and card_num[6] != '4':
        print('Library card is invalid')
        print('The seventh character must be 1 2 3 or 4')
        return False
    check_digit = get_check_digit(card_num)
    value = int(card_num[9])
    if value != check_digit:
        print('Check digit {} does not match calculated value {}'.format(value,check_digit))
        print()
        return False
    else:
        print('Library card is valid')
        return True

if __name__=="__main__":
    string = "Linda Hall"
    new_string = string.center(48)
    string2 = 'Library Card Check'
    new_string2= string2.center(48)
    print(new_string)
    print(new_string2)
    print('='*48)
    print()
    while True:
        card_num = input('Enter Libary Card. Hit Enter to exit ==> ')
        if card_num == '':
            break

        verify = verify_check_digit(card_num)
    
        if verify == True:
            print('The card belongs to a student in {}'.format(get_school(card_num)))
            print('The card belongs to a {}'.format(get_grade(card_num)))
            print()
            