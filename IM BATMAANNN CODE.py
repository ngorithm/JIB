import turtle
#initialize method
b=turtle.Turtle()
#size of pointer and pen
b.turtlesize(1, 1, 1)
b.pensize(3)
#screen info
w=turtle.Screen()
w.bgcolor("YELLOW")
w.title("BATMANNNN")
#colour
b.color("yellow", "black")
#begin filling color
b.begin_fill()
#turn1
b.left(90)   # turn pointer direction to left of 90'
b.circle(50, 85) #draw circle of radius = 50 and 85'
b.circle(15, 110)
b.right(180)
#turn 2
b.circle(30, 150)
b.right(5)
b.forward(10) #draw forward line of 10 units
#turn 3
b.right(90)
b.circle(-70, 140)
b.forward(40)
b.right(110)
#turn 4
b.circle(100, 30)
b.circle(30, 100)
b.left(50)
b.forward(50)
b.right(145)
#turn5
b.forward(30)
b.left(55)
b.forward(10)
#reverse
#turn 5
b.forward(10)
b.left(55)
b.forward(30)
#turn 4
b.right(145)
b.forward(50)
b.left(50)
b.circle(30, 100)
b.circle(100, 30)
#turn 3
b.right(90)
b.right(20)
b.forward(40)
b.circle(-70, 140)
#turn 2
b.right(90)
b.forward(10)
b.right(5)
b.circle(30, 150)
#turn 1
b.left(180)
b.circle(15, 110)
b.circle(50, 85)
#end color filling
b.end_fill()
#end the turtle method
turtle.done()
