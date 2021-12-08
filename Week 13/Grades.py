#CS101 Week 13
#Program  Lab week 13
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##Problem: Create different functions to test   
#ALGORITHM
#1. import math
#2. create function for average that takes values as parameter. Have total equal 0 and then a for loop for the values that addes total plus I then rreturn total
#3. define average function that takes list as parameter. Have total be equal to 0 and then if the length of the list is equal to 0 return math nan. Else for loop the list then add i to total.
#4. then have avgerge equal the total divided by the length of list. Return the averrage
#5. function for median that takes list for parrameter
#6. if not list raise a Value Error. Else have half equal to the length of values divided by 2. use sorted to sort the values then if not legnth of values mod 2 return the values at index halff minus 1
# plus the values at index half divided by 2.
#7. Return the values at half
#8. stop

import math


def total(values):
    total = 0
    for i in values:
        total = total + i
    return total

def average(values):
    total = 0
    if len(values) == 0:
        return math.nan
    else:
        for i in values:
            total = total + i
        avg = total / len(values)
        return avg

def median(values):
    if not values:
        raise ValueError
    else:
        half = len(values) // 2
        values.sort()
        if not len(values) % 2:
            return (values[half - 1] + values[half]) / 2.0
        return values[half]

print(total([4,2,5]))

print(average([4,2,5]))

print(median([2,5,1]))

print(median([2,5,1,3]))