print('Weclome to the Flarsheim Guesser!')
print()
print('Please think of a number between and including 1 and 100.')

play = 'Y'
while play == 'y' or play == 'Y':
    num3 = int(input('What is the remainder when you number is divided by 3?'))
    while (num3 != 2 and num3 != 1 and num3 != 0):
        if num3 > 3:
            print('Enter value less than 3')
        elif num3 < 0:
            print('Enter value greater than 0')
        else:
            ('Error')
        num3 = int(input('What iss  the remainder of your number when divided  by 5?\n'))
    num_5 = int(input('What is the remainder of your number when divided by 5?\n'))
    while num_5 > 5 or num_5 <= 0:
        if num_5 > 5:
            print('The value you entered must be less than 5')
            num_5 = int(input('What is the remainder of your number when divided by 5?\n'))
        elif num_5 <= 0:
            print('The value you entered must be 0 or greater')
            num_5 = int(input('What is the remainder of your number when divided by 5?\n'))
    num_7 = int(input('What is the remainder of your number when divided by 7?\n'))
    while num_7 > 7 or num_7 <= 0:
        if num_7 > 7:
            print('The value you entered must be less than 7')
            num_7 = int(input('What is the remainder of your number when divided by 7?\n'))
        elif num_7 < 0:
            print('The value you entered must be greater than 0')
            num_7 = int(input('What is the remainder of your number when divided by 7?\n'))
        else:
            print('place holder')
    for i in range(0,101):
        if i % 3 == num3 and i % 5 == num_5 and i % 7 == num_7:
            print('Your number was',i)
            print('How amazing was that?')
        else:
            print('place  holder')
    while 1 > 0:
        play = input('Do you want  to play again? (y/n)')
        if play.lower == 'Y' or play.lower == 'N':
            break