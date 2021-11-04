import csv


def  month_from_number(month_int):
    dict1 = {'January':1,'Febuary':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9, 'October':10,'November':11,'December':12}
    try:
        if month_int in range(1,13):
            return(list(dict1.keys())[list(dict1.values()).index(month_int)])
        else:
            raise ValueError
    except ValueError:
        return('Month must be 1-12')
   

def read_in_file(filename):
    file = open(filename, encoding ='utf-8')
    file_csv = csv.reader(file)
    new_list = []
    for line in file_csv:
        new_list.append(line)
    new_list.pop(0)
    file.close()
    return new_list


def create_reported_date_dict(u_lst):
    new_dict = {}
    for i in u_lst:
        if i[1][:2] in new_dict:
            new_dict[i[1][:2]] = new_dict[i[1][:2]] + 1
        else:
            new_dict[i[1][:2]] = 1
    return new_dict

def create_reported_month_dict(u_list):
    new_d = {}
    for i in u_list:
        if i[1][:2] in new_d:
            new_d[i[1][:2]] = new_d[i[1][:2]] +1
        else:
            new_d[i[1][:2]] = 1
    return new_d

def create_offense_dict(u_list):
    new_d = {}
    for i in u_list:
        new_d[i[7]] = new_d.get(i[7],0) + 1
    return new_d

def create_offense_by_zip(u_list):
    new_d = {}
    for i in u_list:
        if i[7] in new_d:
            new_d[i[7]][i[13]] = new_d[i[7]].get(i[13],0) + 1
        else:
            new_d[i[7]] = {i[13]:1}
    return new_d


if __name__== "__main__":
    while True:
        try:
            fname = input('Enter then name of the crime data file ==> ')
            cdf = read_in_file(fname)
            break
        except FileNotFoundError:
            print('Could not fine the file specificed. {} not found'.format(fname))
        except IOError:
             print('Could not fine the file specificed. {} not found'.format(fname))
   
    month_d = create_reported_month_dict(cdf)
    high = 0
    key = ''
    for i in month_d:
        if month_d[i] > high:
            high = int(month_d[i])
            key = int(i)
    print()
    print('The month with the highest # of crimes is {} with {} offenses'.format(month_from_number(key),high))
    offense_d = create_offense_dict(cdf)
    high2 = 0
    key2 = ''
    for i in offense_d:
          if offense_d[i] > high2:
              high2 = offense_d[i]
              key = i
    print('The offense with the highest # of crimes is {} with {} offenses'.format(key,high2))
    print()
    offense_zip = create_offense_by_zip(cdf)
    while True:
        offense_input = input('Enter a offense ')
        if offense_input in offense_zip:
            break
        else:
            print('Not a valid offense found, please try again')
    print()
    print('{} offenses by Zip Code'.format(offense_input))
    print('{:<10}{:>10}'.format('Zip Code','# Offenses'))
    print('='*20)
    for k,v in offense_zip[offense_input].items():
        print(f'{k:<10}{v:>10}')
