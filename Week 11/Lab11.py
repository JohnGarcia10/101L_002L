#CS101 Week 11
#Program  Lab week 11
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##Problem: Open a file from user input and ouptut the frequncey of the words and how many times a word appears once
#ALGORITHM
#1. start 
#2. import time module, begin set up for class Clock
#3. Create init that takes hours, minutes, seconds, and clock type that has a deafult value of 0
#4. set self of each instance passed to its self, (ex. self.hour = hours)
#5. set a __str__ to return clock time, if the type is 0 just print out the hours, minutes, seconds
#6. if  hours is greater than 12 print same format but with pm and hours minus 12
#7. elif hours equals 12 print same format but have the hours just be 12 
#8. elif hours is equal to 0 print same format as last step but as am 
#9. else return same format as step 5 with am 
#10. define a tick function inside Clock class that incremetes self seconds by one, and if seconds equal 60 increment minutes by 1 and set seconds  back to 0
#11. if minutes equal 60 increment hours by 1 and set minutes and seconds to 0 
#12. in the main as user input for hours, minutes, seconds
#13. set variable equal to Clock with the parameters of hours, minutes, and seconds for the class
#14. create infinte loop that prints varibale from step 13, also have that variable with the tick function from class, and have time.sleep(1) from module 
#15. stop

import time
class Clock():
    def __init__(self,hours,minutes,seconds,clock_type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.type = clock_type
    
    def __str__(self):
        if self.type == 0:
            return "{:02}:{:02}:{:02}".format(self.hours,self.minutes,self.seconds)
        elif self.hours > 12:
            return "{:02}:{:02}:{:02} pm".format(self.hours - 12,self.minutes,self.seconds)
        elif self.hours == 12:
            return "{:02}:{:02}:{:02} pm".format(12,self.minutes,self.seconds)
        elif self.hours == 0:
            return "{:02}:{:02}:{:02} am".format(12,self.minutes,self.seconds)
        else:
            return "{:02}:{:02}:{:02} am".format(self.hours,self.minutes,self.seconds)
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1 
                self.minutes = 0
                self.seconds = 0

if __name__ == '__main__':
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the currrent second ==> '))

    clock = Clock(hours, minutes, seconds,1)

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)