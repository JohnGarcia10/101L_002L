d = {'A':1, 'B':2, 'C': 3}

user_key = input('Enter a key')

for k, v in d.items():

    if k == user_key:

         print(user_key[v])

    else:

         print('Not found')