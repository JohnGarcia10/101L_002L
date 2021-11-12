def file():
    while True:
        try:
            fname = input('Enter a file --> ')
            file = open(fname,'r')
            line = file.read()
            for i in line:
                print(i)
            break
        except FileNotFoundError:
            print('Could not open file {}'.format(fname))

