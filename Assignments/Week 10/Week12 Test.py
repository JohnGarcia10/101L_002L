def file():
    while True:
        try:
            fname = input('Enter a file --> ')
            file = open(fname,'r')
            dict1 = {}
            content = ' '.join(line for line in file.read().splitlines())
            content =content.split(' ')
            dict1 = {}
            for word in content:
                if  word not in dict1:
                    dict1[word] = 1
                else:
                    dict1[word] += 1
            for key in list(dict1.keys()):
                print("{:<5} {:<10}  {:<10}".format(1,key,dict1[key]))
                print(key,':',dict1[key])
            break

        except FileNotFoundError:
            print('Could not open file {}'.format(fname))



file()
