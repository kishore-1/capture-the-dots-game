import turtle
import random
import math
import winsound
a=turtle.Screen()
a.bgcolor("dark blue")
a.tracer(4)
a.bgpic("pic1.jpg")
pen=turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
pen.pencolor("white")
bond=turtle.Turtle()
bond.penup()
bond.speed(0)
bond.goto(-350,-290)
bond.pendown()
bond.pensize(3)
bond.pencolor("white")
for i in range(2):
    bond.forward(700)
    bond.left(90)
    bond.forward(580)
    bond.left(90)
bond.hideturtle()
player=turtle.Turtle()
player.color("blue")
player.shape("classic")
player.turtlesize(2)
player.penup()
mgoal=6
goal=[]
for i in range(mgoal):
    goal.append(turtle.Turtle())
    goal[i].shape("circle")
    goal[i].color("red")
    goal[i].turtlesize(0.5)
    goal[i].penup()
    goal[i].speed(0)
    goal[i].goto(random.randint(-350,350),random.randint(-290,290))
    goal[i].right(random.randint(0,360))
speed=1
player.speed(0)
def up():
    global speed
    speed +=0.5
def down():
    global speed
    speed -=0.5
def left():
    player.left(30)
def right():
    player.right(30)
turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
score=0
while True:
    player.forward(speed)
    for i in range(mgoal):
        goal[i].forward(1.5)
        if (goal[i].xcor() > 340 or goal[i].xcor() <-340):
            goal[i].right(55)
        if (goal[i].ycor() > 280 or goal[i].ycor() <-280):
            goal[i].right(55)
        d=math.sqrt(math.pow(player.xcor()-goal[i].xcor(),2)+math.pow(player.ycor()-goal[i].ycor(),2))
        if d<15:
            winsound.PlaySound("Pat-SoundBible.com-1661659465.wav",winsound.SND_ASYNC)
            score+=1
            goal[i].goto(random.randint(-350,350),random.randint(-290,290))
        pen.undo()
        pen.penup()
        pen.pencolor("white")
        pen.goto(-290,300)
        string="Score=%s"%(score)
        pen.write(string,False,align="left",font=("Arial",14,"bold"))
        if (player.xcor() > 350 or player.xcor() <-350):
            speed=0
            pen.penup()
            pen.goto(160,300)
            pen.pencolor("white")
            string="Game over"
            x=1
            pen.write(string,False,align="left",font=("Arial",14,"bold"))
            if x==1:
                winsound.PlaySound("Explosion+1.wav",winsound.SND_ALIAS)
                end()              
        if (player.ycor() > 290 or player.ycor() <-290):
            speed=0
            pen.penup()
            pen.goto(160,300)
            pen.pencolor("white")
            string="Game over"
            x=1
            pen.write(string,False,align="left",font=("Arial",14,"bold"))
            if x==1:
                winsound.PlaySound("Explosion+1.wav",winsound.SND_ALIAS)
                end()         
delay=input("Enter to finish") 
