#CS101 Week 12
#Program  Lab week 12
#Jonathan Garcia Sanchez
#jggfh@umsystem.edu
##Problem: Use turtle to draw different objects 
#ALGORITHM
#1. start
#2. import turtle module
#3. define class for Point that passes x y and color in constructor
#4. class function for drawing the point that uses turtle penup, then go to the self x and y put pen down, color the point with self color and set a heading for 0. At the end have self draw action at the end
#5. define another class function for draw action that passes self and contains turtle dot 
#6. create another class for box that passes point and the init constructor contains x1 y1 width height and color. Also have a super init that passes the init from Point class 
#7. Create class function for a draw action put into a loop for the range of 2. Inside the loop make it have the turle backward that passes self width, the go right 90, backward by self height then right 90 again
#8. Create another class called BoxFilled that passes box inside  the init pass x1 y1, width height color and fillcolor. Also pass super init that the box class had and then have self fillcolor
#9. Create a function in that class for draw action that passes self and then uses turtle moduel to fill color with the self fill color and call the draw action  and  ends the fill
#10. Create class for Circle that passes point that passes x1 y1 radius and color then have  radius be self radius. Create function for draw action that uses turtle circle
#11. class for CircleFilled that passes Circle with an init of x1 y1 radius color and fillcolor. And a function for draw action that fills by the self fill 
#12. In the main call the class in a variable then use that variable to draw 
#13. Stop

import turtle

class Point():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self,x1,y1,width,height,color):
        super().__init__(x1,y1,color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        for i in range(2):
            turtle.backward(self.width)
            turtle.right(90)
            turtle.backward(self.height)
            turtle.right(90)

class BoxFilled(Box):
    def __init__(self,x1,y1,width,height,color,fillcolor):
        super().__init__(x1,y1,width,height,color)
        self.fill = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fill)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self,x1,y1,radius,color):
        super().__init__(x1,y1,color)
        self.radius = radius
    
    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self,x1,y1,radius,color,fillcolor):
        super().__init__(x1,y1,radius,color)
        self.fill = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fill)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()







p = Point(-100,100,'blue')
p.draw()

b=Box(200,210,150,140,'red')
b.draw()

b1=BoxFilled(200,210,150,140,'green','blue')
b1.draw()

c = Circle(-200,210,50,'green')
c.draw()

c1 = CircleFilled(-200,210,50,'green','red')
c1.draw()