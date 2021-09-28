#Jonathan Garcia Sanchez
#CS101-02
#Program 2
#Created 10-26-2021
import random 
isTrue = True 
while isTrue == True:
    print('Round: 1')
    x = int(1)
    y = int(6)
    dice1 = random.randint(x,y)
    dice2 = random.randint(x,y)
    total = dice1 + dice2
    print('First dice:', dice1)
    print('Second dice:', dice2)
    round = 1
    if dice1 == dice2:
        print('** COMPUTER WON!!**')
        print('First dice ==  Second dice after',round,'round')
    round = 2
    while dice1 != dice2:
        print('Round:',round)
        print("First dice", dice1)
        dice2 = random.randint(x,y)
        print("Second dice", dice2)
        if dice1 == dice2 and round < 3:
            print('** COMPUTER WON!!**')
            print('First dice ==  Second dice after',round,'round')
            print('Total is', total)
        elif dice1 == dice2 and round >= 3:
            print('Computer Lost this Turn')
            print('First dice ==  Second dice after',round,'rounds')
        round = round + 1
    active = True
    while True:
            prompt = input('Do you want to paly again? (Y/y)')
            if prompt.lower() == 'y':
                break
            elif prompt.lower() == 'n':
                active = False
                print('Have a great day')
                break
            else:
                print('You must input a valid option!')
    isTrue = active
                        
