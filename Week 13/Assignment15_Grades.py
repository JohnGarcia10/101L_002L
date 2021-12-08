#CS101 Week 13
#Program  Lab week 13
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##Problem: Use the unittest 
#ALGORITHM
#1. start 
#2. import unittest, import grades, and imporrt math
#3. create class for grade test and pass unitest 
#4. create a function for the return of total then inside have result equal to Grades total function with a list. Asset equal with the result and 33 as the answer 
#5. create functionh for return of 0 that passes with an empty list and asserts equal with result and 0
#6. Function for testing average using the Grade average function and using assertalmost equal 
#7. Create another function for testing average of two and assertly with almost equal with what the results hsould be 
#8. Function forr testing average return of nan using math import with an empy list and average
#9. function for testing median of one with a list and Grades median with  again assertEqual with what the rresults hsould be 
#10. Anotherr function for testing median with two and calls median then use assertequal with what the answers should be
#11. last function for return median rerturn of ValueErrror that rasies Value error if empty 
#12. in the main call unittest main
#13. stop

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,33,'The  total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result,0,'The total should return 0')

    def test_average_one(self):
        result  = Grades.average([2,5,9])
        self.assertAlmostEqual(result,5.33333,5)
    
    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12,1)
    
    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(math.nan,result,'The average function should return nan when passes an empty list')
    
    def test_median_one(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result,2)
    
    def test_median_two(self):
        result = Grades.median([5,2,1,3])
        self.assertEqual(result,2.5)

    def test_median_returns_ValueError(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])

unittest.main()