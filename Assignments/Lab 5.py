#CS101 Lab 5 
#Program  Lab 5
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
#PROBLEM: Fill out functions that are given to create a slot machine with 3 reels, with each being 1-10. User  chooses the chip amount to start and they wager between 1 to the amount bankif 3 they win 10 times wager, 2 will win 3 times,. 
###
#1. start
#2. import random module
#3. set up play again function, set a while true then ask for input if they want to play again. If they input y or yes return true, if they input n or no return false. Otherwise print that they must under Y/Yes/N/No and try again. Contnnue
#4. Set up get wager function, ask user for starting chip amount. Begin a while true loop then if to check if the input amount is greater than 0 and less/equal to bank return start chip amount. \
#5. if start chips is less than 0 print amount should be greater and try again, else print it cannot be greater and ask again
#6. Set up the get results function as tuple, here return 3 random randints between 1 and 10
#7. Set up get matches, first if statement if reela,reelb, and reelc are equal to each other return 3.If two are equal to each other return 2, otherwise return 0
#8.Next set up function is get bank, begin while true loop. Inside ask for the amount of chips the user wants to begin with. Make if statements for the input, if input is greater than 0 but less than 101 return input.
#9. If input is less than 0  print to low of value and try again, if greater than 101 print to  high and try again
#10. Last funtion set up is get payout, if matches equals 3 then return 10 times the wager amount, if matches equals 2 return 3 times the wager, and if matches = 0 return wager times-1
#11.In the main now set up playing equal to True then create  while loop for the playing.
#12. Inside make bank equal to get bank function, creatre spins equal to 0, create variable chip max equal to bank, then create varibale start chip equal to bank
#13. While still inside set up another while loop for bank being greater than 0
#14. Inside this loop create wager variable equal to get wager function with bank as parameter
#15. Create reel1,reel2,reel3 together equal to get results 
#16. Create 3 more variables being matches equal to get matches with reel1,reel2,reel3 being the parameters. Next variable is payout to be equal to get payout with parameters wager and matches. Last one is bank equal to bank + payout
#17. Set spins equal to spins plus 1
#19. Then have if statement if bank is greater than chip max, inside this if set chip max eqal to bank. Then print your spin with the reels 1,2,3. Print you matched with matches varible. Print  You won/lost with payout varible, and print current bank with bank variable
#20. Outside the while bank greater than 0 loop print you lost, start bank variable, in, spins variable, spins. Then print the most chips you had was, chip max varible
#21. set playing equal to play again function
#22. stop


import random
def play_again() -> bool:
    '''Ask the user if they want to play again, returns False  if N or NO, True if Y or YES. Keeps asking until they respond yes'''
    while True:
        x = input('Do you want to play again? ==>').lower()
        if x == 'y' or x == 'yes':
            return True
        elif x == 'n' or x == 'no':
            return False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            continue


def get_wager(bank : int) -> int:
    '''Asks the user for wager chip amount. Contines to ask if they results is <= 0 or greater than the amount they have'''
    start_chips = int(input('How many chips do you want to wager? ==>'))
    while True:
        if 0 < start_chips <= bank:
            return start_chips
        elif start_chips <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
            start_chips = int(input('How many chips do you want to wager? ==>'))
        else:
            print('The wager amount cannot be greater than how much you have.', bank)
            start_chips = int(input('How many chips do you want to wager? ==>'))



def get_slot_results() ->  tuple:
    '''Returns the result of the slot pull'''
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)


def get_matches(reela, reelb, reelc) -> int:
    '''Returns 3 for all 3 match, 2 for alike, and 0 for none alike'''
    if reela == reelb == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else: 
        return 0


def get_bank() ->  int:
    '''Returns how many chips the user wants to play with. Loops until a value greater than 0 and less than 101'''
    while True:
        chips = int(input('How many chips do you want to start with? ==>'))
        if 0 < chips < 101:
            return chips
        elif chips <= 0:
            print('Too low a value, you can only choose 1 - 100 chips'.format(chips))
        elif chips > 101:
            print('Too high a value, you can only choose 1 - 100 chips'.format(chips))





def get_payout(wager, matches):
    '''Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the ager if 2 match, and negative wager if 0 match'''
    if matches == 3:
        return 10 * wager
    elif matches == 2:
        return 3 * wager
    elif matches == 0:
        return wager *-1


if __name__ == '__main__':
    playing = True
    while playing:

        bank = get_bank()
        spins = 0
        chip_max = bank
        start_bank = bank

        while bank > 0:

            wager = get_wager(bank)

            reel1,reel2,reel3= get_slot_results()

            matches = get_matches(reel1,reel2,reel3)
            payout = get_payout(wager,matches)
            bank =  bank +  payout
            spins = spins +  1
            if bank > chip_max:
                chip_max = bank

            print('Your spin', reel1,reel2,reel3)
            print('You matched',matches,'reels')
            print('You won/lost',payout)
            print('Current bank',bank)
            print()

        print('You lost all',start_bank,'in',spins,'spins')
        print('The moost chips you had was',chip_max)
        playing = play_again()