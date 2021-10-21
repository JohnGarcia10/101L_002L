#CS101 Lab 5 
#Program  Lab 5
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
###PROBLEM: Create a cipher where the user will get a choice between encrypting or decrypting a code. If user chooses to encrypt ask for the text they want to encrypt and by what number they want to shift that by
#then in the code have a series of loops that go through each index of the text and shift them by the amount input by the user. If they choose to decrypt repeat steps except shift them in the opposite way. Ask the same menu again and if they hit Q they quit or they can choose to repeat etiher encyrpt or decyrpt. 
####
#1. start 
#2. import the string module 
#3. Make first function for encrypt that takes string text and int key as parameters
#4. Inside set a string1 equal to '' then set letters to string ascii uppercase 
#5. Start a for loop for i in string text, then an if inside for i in letters, inside that have an if for string ascii lowercase index of i. lower plus 1 plus the int key being greater than 25
#6. if that if from 5 is ture then set a number letter variable equal to string ascii lowercase index of i.lower plus int key minus 26
#7. i will equal letters at number letter index
#8. outside that if have an else for i being equal to letters at index string ascii lowercase index(i.lower) plus the int key 
#9. outside of that have string1 equal plus i, then outside of that have an  else for string1 plus i again, finally outside of that return string1
#10. Begin next function for dectyrtion that takes same string text and int key variables
#11. repeat steps 4-9, only from step 5 change the 1 plus int key to 1 mius int key greater than 25. And in from step 6 instead of having plus int key minus 26,  have minus int key - 26
#12 set up new function for get input, ask user for an input selection and while loop if the user input is not 1,2,3, or Q to ask again 
#13.  return user input 
#14. set up main menu function to print the menu of selections 
#15. set up main function, inside have choice equal to true
#16. being while for choice, inside have main menu function 
#17. have choice1 variable equal to get input function 
#18. have an if statement if choice1 equals 1, inside the if have an user input on what brief stament they want to encrypt 
#19. have user input for the int key to shift letters by, then have encryption variable equal the encrypt function with both the user  inputs of text and key as parameters 
#20. print the encytption 
#21. outside that if have an elif for choic1 if it equals 2 then repeat the same steps only replace the enctyption with the decytption variables 
#22. outside that elif have another for if choice1 is Q then break the program 
#23. finally have the main at the bottom outside everything to show program run
#24. stop

import string

def c_encrypt(string_x, key):
    string1 = ''
    letters = string.ascii_uppercase
    for i in string_x:
        if i in letters:
            if (string.ascii_lowercase.index(i.lower()) + 1 + key) > 25:
                num_letter = string.ascii_lowercase.index(i.lower()) + key - 26
                i = letters[num_letter]
            else: 
                i = letters[string.ascii_lowercase.index(i.lower()) + key]
            string1 +=  i
        else:
            string1 += i
    return string1
            

def c_decrypt(string_x, key):
    string1 = ''
    letters = string.ascii_uppercase
    for i in string_x:
        if i in letters:
            if (string.ascii_lowercase.index(i.lower()) + 1 - key) > 25:
                num_letter = string.ascii_lowercase.index(i.lower()) - key - 26
                i = letters[num_letter]
            else:
                i = letters[string.ascii_lowercase.index(i.lower()) - key]
            string1 += i
        else:
            string1 += i 
    return string1

def get_input():
    user_input = ('Enter your selection ==> ')
    while user_input not in ('Q','1','2'):
        user_input = input('Enter your selection ==> ')
    return user_input

def main_menu():
    print('MAIN  MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

def main():
    choice = True 
    while choice:
        main_menu()
        print()
        choice1 = get_input()
        print()
        if choice1 == '1':
            e_text = input('Enter (brief) text to encrypt: ').upper()
            num_key = int(input('Enter the number to shift letter by: '))
            encryption = c_encrypt(e_text, num_key)
            print('Encrypted:',encryption)
            print()
        elif choice1 == '2':
            d_text = input('Enter (brief) text to decrypt: ').upper()
            num_key = int(input('Enter the number to shift letter by: '))
            decryption = c_decrypt(d_text, num_key)
            print('Decrypted:',decryption)
            print()
        elif choice1 == 'Q':
            break

main()