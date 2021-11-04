#CS101 Lab  Week 10
#Program Lab Week 10
#Jonathan Garcia  Sanchez
#jggfh@umsystem.edu
##Problem: Read through a CSV file and use dictionaries to go through the file and output the month with the highest crimes and the offense with the highest crime
#Be able  to show the offense the user inputs 
#1. start
#2. Import csv module
#3. set up function for month that inside has a dict with the months with what number they are, try if the month is in range of 1-13 then return list of the keys with the values and index to show the month 
#4. else raise a value error in the except 
#5. have a read in file function that takes the  file  name from the user
#6. open the file name with endcoing utf-8, use csv reader to read through the file, make a new list then a for loopo for line in the csv reader
#7. append the line to the new list and pop at 0, close the file
#8. Make a function for reported date dicitonary that takse list parameter, have a new empty dict.
#9. Have a for loop for the list passed and if the i at the 1 slicing throug h2 in the new dict have new dictionary of index i at  1 and :2 equal new d at the same thing plus 1
#10. else have that equal 1 then return new d
#11. Another function for the offense dictiontary that takes a list, have an empty dictionary then for loop for i in the list
#12. have new_d at i index 7 equal to new.get of i[7] plus 1, then return new d 
#13. function for offense by zip that takes a list, set up empy dictiionary, and iterarte through the list
#14. if at i index 7 in the new d  then have new d of i index 7 and i index 13 equal new d of i index 7 get the i index 13 plus 1
#15. eluse have it equal i index  13 slice: 1
#16. In the main have a while true, then a try
#17. Ask user for input ofr name of data  file, then call the read in file function to equal a vairbale (CDF), except a file not found and  iO error
#18. have a variable for month_d equal the create reported month dict function with the CDF  
#19. have the highest equal 0, and a key equal '' then iterate for i in the month_d. If at the index i being greater than the highest amount, then have high equal the month at the i index as in int. Have key be equal to int i 
#20. print the month with high crime with format of the month from number function that takes the key from last step and the highest to print
#21. do one for offense_d that will equal the create offense dict function that takes cdf from earlier
#22. same repeat with highest equal to 0 and key equal to '' then iterate for i in the offense_d. If the offense at i index is greater than the highest again have highest equal offense at i index and key equal to i
#23. print the same way as step 20 but whth the new key and highest 2
#24. Have an offense zip that equal the create offense by zip with cdf as the parameter
#25. While true that ask user for offense input and if  the input is in the offense zip break. Else print its not found 
#26. print the offense iput by zip code, print the zip code  and # of offense then print the key and value paries using a for loop and .items for offense zip
#27. stop

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
