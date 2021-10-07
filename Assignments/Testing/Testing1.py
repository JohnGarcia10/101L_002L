'''def get_wager(bank : int) -> int:
    Asks the user for awager chip amount. Contines to ask if they results is <= 0 or greater than the amount they have
    while True:
        chips = int(input('How many chips do you want  to start with? ==>'))
        if chips < 0:
            print('Too low a value, you can only  choose 1 -',bank,'chips')
        elif chips > bank:
            print('Too high a value, you can only choose 1 -',bank,'chips')
        else:
            return chips

get_wager(100)'''
'''import random 
def get_slot_results() ->  tuple:
    Returns the result of the slot pull
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)

get_slot_results()'''

def get_bank() ->  int:
    '''Returns how many chips the user wants to play with. Loops until a value greater than 0 and less than 101'''
    start_chips = int(input('How many chips do you want to wager? ==>'))
    while True:
        if 0 < start_chips < 101:
            return start_chips
        elif start_chips <= 0:
            print('The wager amount must be greater than 0. Please enter again')
            start_chips = int(input('How many chips do you want to wager? ==>'))
        else:
            print()

'''Asks the user for awager chip amount. Contines to ask if they results is <= 0 or greater than the amount they have'''
    while True:
        chips = int(input('How many chips do you want to start with? ==>'))
        if chips < 0:
            print('Too low a value, you can only  choose 1 -',bank,'chips')
        elif chips > bank:
            print('Too high a value, you can only choose 1 -',bank,'chips')
        else:
            return chips