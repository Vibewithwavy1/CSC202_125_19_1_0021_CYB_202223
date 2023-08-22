#Day 18 - Turtle
import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

colors = ["red","purple","black","green","yellow","gray","brown"]
direction = [0, 90, 180, 360]
tim.pensize(15)
tim.speed(1)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))
  
#Turtle Square
# print(another.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
#turtle will move in square dimension
my_screen = Screen()
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
for a in range(4):
    timmy.forward(200)
    timmy.right(90)

print(my_screen.canvwidth)
print(my_screen.canvheight)
#my_screen is object and canvwidth is the attribute
my_screen.exitonclick()