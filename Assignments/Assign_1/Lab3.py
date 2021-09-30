#CS101 LAB 3 
#Lab 3 
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##
#Have user guess a number then input the remainder when the number is divided 3, 5, and 7 then have it go through checking if it is divisble by it
#1. start,  2. print the welcome to the guesser then set up a variable to play again as y
#3. set up while loop for the a yes input then as print for a guess of 1 - 100
#4. ask user input for what the number is remainder of 3 
#5. Start a while loop for that input if it is greater or equal to 3 or less than 0
#6. If elif statement based on if lower than 3 or less than 0 to print to input new number 
#7. repeat steps 4-6 for numbers 5 and 7 
#8. Set up for loop for numbers in range or 1-101, then have an if inside for a number i to equal mod of 3, 5, 7
#9. print i as the number they were thinking of 
#10. have a while for anything true like 1  being greater than 0 then ask for input if user wants to play again
#11. Set if  inside  after if  the input is y, Y, n, N then break 

print('Weclome to the Flarsheim Guesser!')
print()

play = 'y'
while play == 'y' or play == 'Y':
    print('Please think of a number between and including 1 and 100.')
    print()
    num3 = int(input('What is the remainder when you number is divided by 3?'))
    print()
    while num3 >= 3 or num3 < 0:
        if num3 >= 3:
            print('The value entered must be less than 3')
            num3 = int(input('What is the remainder when your number is divided by 3?'))
        elif num3 <= 0:
            print('The value you entered must be 0 or greater')
            num3 =  int(input('What is the reaminder  when your number is divided by 3?'))
    num_5 = int(input('What is the remainder of your number when divided by 5?'))
    print()
    while num_5 > 5 or num_5 < 0:
        if num_5 >= 5:
            print('The value you entered must be less than 5')
            num_5 = int(input('What is the remainder of your number when divided by 5?'))
        elif num_5 <= 0:
            print('The value you entered must be 0 or greater')
            num_5 = int(input('What is the remainder of your number when divided by 5?'))
    num_7 = int(input('What is the remainder of your number when divided by 7?'))
    while num_7 > 7 or num_7 < 0:
        if num_7 >= 7:
            print('The value you entered must be less than 7')
            num_7 = int(input('What is the remainder of your number when divided by 7?'))
        elif num_7 <= 0:
            print('The value you entered must be greater than 0')
            num_7 = int(input('What is the remainder of your number when divided by 7?'))     
    for i in range(0,101):
        if i % 3 == num3 and i % 5 == num_5 and i % 7 == num_7:
            print('Your number was',i)
            print('How amazing was that?')
    print()
    while 1 > 0:
        play = input('Do you want  to play again? (y/n)')
        if play == 'Y' or play == 'y' or play == 'n' or play == 'N':
            break