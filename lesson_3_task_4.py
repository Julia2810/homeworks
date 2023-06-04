from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)
my_turtle.screen.bgcolor("violet")
my_turtle.pensize(10)



#тело
my_turtle.penup()
my_turtle.goto(0, -300)
my_turtle.pendown()
my_turtle.circle(150)

#голова
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
my_turtle.circle(100)


#уши
my_turtle.penup()
my_turtle.goto(50, 190)
my_turtle.pendown()
my_turtle.right(300)
my_turtle.forward(50)
my_turtle.goto(80,160)
my_turtle.penup()
my_turtle.goto(-50, 190)
my_turtle.pendown()
my_turtle.right(300)
my_turtle.forward(50)
my_turtle.goto(-80,160)

#глаза
my_turtle.penup()
my_turtle.goto(50, 150)
my_turtle.pendown()
my_turtle.circle(10)

my_turtle.penup()
my_turtle.goto(-50, 150)
my_turtle.pendown()
my_turtle.circle(10)

#усы
my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(100)
my_turtle.forward(80)

my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(30)
my_turtle.forward(80)

my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(30)
my_turtle.forward(80)


my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(100)
my_turtle.forward(80)

my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(30)
my_turtle.forward(80)

my_turtle.penup()
my_turtle.goto(0, 100)
my_turtle.pendown()
my_turtle.right(30)
my_turtle.forward(80)

#рот
my_turtle.penup()
my_turtle.goto(0, 70)
my_turtle.pendown()
my_turtle.color("red")
my_turtle.begin_fill()
my_turtle.circle(17)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(0, 75)
my_turtle.pendown()
my_turtle.color("violet")
my_turtle.begin_fill()
my_turtle.circle(17)
my_turtle.end_fill()

#правая лапа
my_turtle.penup()
my_turtle.goto(210, -70)
my_turtle.pendown()
my_turtle.color("black")
my_turtle.begin_fill()
my_turtle.left(40)
for i in range(2):
    my_turtle.forward(75)
    my_turtle.right(90)
    my_turtle.forward(7)
    my_turtle.right(90)
my_turtle.end_fill()


#левая лапа
my_turtle.penup()
my_turtle.goto(-135, -85)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.right(40)
for i in range(2):
    my_turtle.forward(75)
    my_turtle.right(90)
    my_turtle.forward(7)
    my_turtle.right(90)
my_turtle.end_fill()

#правая нога
my_turtle.penup()
my_turtle.goto(150, -320)
my_turtle.pendown()
my_turtle.color("black")
my_turtle.begin_fill()
my_turtle.right(30)
for i in range(2):
    my_turtle.forward(75)
    my_turtle.right(90)
    my_turtle.forward(7)
    my_turtle.right(90)
my_turtle.end_fill()

#левая нога
my_turtle.penup()
my_turtle.goto(-150, -320)
my_turtle.pendown()
my_turtle.color("black")
my_turtle.begin_fill()
my_turtle.right(90)
for i in range(2):
    my_turtle.forward(75)
    my_turtle.right(90)
    my_turtle.forward(7)
    my_turtle.right(90)
my_turtle.end_fill()



my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()