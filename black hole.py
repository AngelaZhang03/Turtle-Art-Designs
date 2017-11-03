import turtle
bob = turtle.Turtle()
turtle.bgcolor("Midnight Blue")
bob.speed(0)
for i in range(720):
    bob.forward(50)
    bob.right(15)
    bob.forward(250)
    bob.setpos(0,0)
    bob.left(15.5)
from turtle import*
def drawStar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

color("WhiteSmoke")
for times in range(20):
    drawStar()
    forward(100)
    drawStar()
    left(120)
    forward(150)
    drawStar()

hideturtle()
done()



     






    



    
