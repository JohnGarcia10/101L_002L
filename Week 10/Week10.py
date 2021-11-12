#CS101 Week 11
#Program  Lab week 11
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##Problem: Open a file from user input and ouptut the frequncey of the words and how many times a word appears once
#ALGORITHM
#1. start 
#2. set up while true that has a try for asking input to open a file and read it, except a filenotfound error
#3. split the contents into words
#4. function for clean words that strips words for !. and appends those stripped words to a list 
#5. function for frequncey that has empty dictionary and empty list and a counter equal to 0
#6. loop through the list of new words that gets each word at index of frequncey plus 1 now print word and freq to add to dictionary 
#7. loop for items in frequncey that adds one to counter and prints each one in frequncey 
#8. then loop for values at  are equal to one and  add to list then print how many words occur once from the len of list 
#9. function for unique words that loops through new words list and appends word to an empty set then print based on the length 
#10. stop
while True:
    try:
        fname = input('Enter the name of the file to open ')
        file = open(fname,'r')
        contents = file.read()
        words = contents.split()
        file.close()
        break
    except FileNotFoundError:
        print('Cound not find {} file'.format(fname))
        print('Please Try Again')
        print()
        


def clean_words(words):
    words = [i.strip('!.') for i in words]
    new_words  = []
    for i in words:
        i.strip('!.')
        if len(i) > 3:
            new_words.append(i)
    for i in range(len(new_words)):
        new_words[i] = new_words[i].lower()
    return  new_words

def frequencey(new_words):
    global freq
    freq  = {}
    once = []
    counter = 0
    for i in new_words:
        freq[i] = freq.get(i,0)+1
    print()
    print('Most frequently used words')
    print('{:<5} {:<15} {:<15}'.format('#','Word','Freq.'))
    print('='*35)
    for k,v in freq.items():
        counter += 1
        print('{:<5} {:<15} {:<15}'.format(counter,k,v))
    for v in freq.values():
        if v == 1:
            once.append(v)
    print('There are {} words that occur only once'.format(len(once)))
        
                



    
def unique(new_words):
    u_set = set()
    for i in new_words:
        if i not in u_set:
            u_set.add(i)
    print('There are {} unique words in the document'.format(len(u_set)))
    
new_words = clean_words(words)
frequencey(new_words)
unique(new_words)