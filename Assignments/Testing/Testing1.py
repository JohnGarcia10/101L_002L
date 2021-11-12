'''1- Write a function that takes a list and returns a new list
with unique elements of the first list.
e.g: [1,2,3,1,4,3,2,6,8,6] -->[1, 2, 3, 4, 6, 8] Do not use sets'''

def unique(list):
     new_list = []
     for i in list:
          if i not in new_list:
               new_list.append(i)
          else:
               continue
     return new_list

lst = [1,2,3,1,4,3,2,6,7,6]
print(unique(lst))

'''2- Write program to create a dictionary from two given lists:'''
class_list = ['CS201', 'CS101', 'CS191', 'IT222']
id_list = [1, 2, 2, 3]

new_dict = dict(zip(class_list,id_list))
print(new_dict)

'''3- Given n=range(-5,5), by using filter(fun,seq) save all negative numbers
in n to a list'''

new_list = list(filter(lambda i:i<0, range(-5,5)))
print(new_list)

'''4- By using py_dict, write program to save key:value in new dictionary
without having duplicates for values '''
'''py_dict={'a':10,'b':20,'c':10,'d':30,'e':20}'''
#output: new = {'a':10,'b':20,'d':30}

py_dict={'a':10,'b':20,'c':10,'d':30,'e':20}
new_d = {}
for k,v in py_dict.items():
     if v not in new_d.values():
          new_d[k] = v
     else:
          continue
print(new_d)

'''5- Write program to declare a set with values from 0 to 5
and delete the value 4 if exist in set'''

new  = set(range(0,6))
print(new)

new_s = set(filter(lambda x: x != 4, new))

print(new_s)

lst  = [1,2,3,4,5,6]
for i in range(1,6):
     lst[i-1] = lst[i]
for i in range(0,6):
     print(lst[i], end=' ')