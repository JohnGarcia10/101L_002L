'''Example 1:Define class Employee with two instance attributes wage
and hours_worked and set each to 0.
Also define calculate_pay method.The method should return the amount
to pay the employee, by multiplying the employee's wage and number of hours
worked. '''

'''class Employee:
     def __init__(self,wage = 0, hours_worked = 0):
          self.wage = wage
          self.hours = hours_worked
     
     def calculate_pay(self):
          pay = wage * hours_worked
          return pay
wage = int(input('Enter your wage: '))
hours_worked = int(input('Enter your hours worked: '))

work = Employee(wage,hours_worked)
print(Employee.calculate_pay(work))'''

'''Example 1:Overloaded operators
Define class Point that will have two instance attributes x and y.
Set default values for both to 0. Add necessary methods to add two objects
of class,also method to print all details about object of class'''

class Point:
     def __init__(self,x=0,y=0):
          self.x = x
          self.y = y
     def __add__(self,other):
          sumx = self.x + other.x
          sumy = self.y + other.y
          return Point(sumx,sumy)
     def __str__(self):
          return 'Values are {} {}'.format(self.x,self.y)
     def get_x(self):
          return self.x

p1 = Point(10,20)
p2 = Point(20,30)
p3 = p1 + p2
print(p3)
print(p1.get_x())

'''Example 2: Overloaded operators
Define class Circle that will include constructor with instance attribute
radius with default value 0, getter(return value), setter( set some values)
and area method to output area of circle.
Also include overloaded operator <,> to compare two objects of the class.'''

class Circle:
     def __init__(self, radius = 0):
          self.r = radius
     def set_v(self,other):
          self.r = other
     def get_value(self,other):
          return self.r
     def __lt__(self,other):
          return self.r < other.r
          