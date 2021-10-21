import random

def question(words):
    num_ques = 1
    score = 0
    while num_ques < 4:
        res = key, val = random.choice(list(words.items()))
        global q1
        q1 = res[0]
        global a1
        a1 = res[1]
        print('Question {} :'.format(num_ques))
        print()
        print('What is',q1,'in Latin')
        x = input('==> ')
        if num_ques == 4:
            break
        if x == a1:
            print('Correct')
            num_ques += 1 
            score += 1
        else:
            print('incorrect')
            num_ques += 1
    print('You got {} correct answer(s)'.format(score))
        
def play_again():
    while True:
        z = input('Do yo want to play again: Y/y or N\n').lower()
        if z == 'y' or z == 'Y':
            return True
        elif z == 'n' or z == 'N':
            print('Have a great day')
            break


        

if __name__ == '__main__':
    words = {'water':'aqua','good':'bene','before noon':'ante meridiem','in fact':'de facto','I':'ego','sea':'mare','afternoon':'post meridian'}
    playing = True 
    while playing:
        print('Ready for your Quiz')
        print()
        question(words)
        playing = play_again()



