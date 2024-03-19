import turtle as t
import math
import random
import time

t.tracer(0)      
t.hideturtle()   


#circle
def draw_circle(color, fill_color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#eye
def draw_eye(color, fill_color, radius, x, y):
    t.fillcolor(fill_color)
    t.begin_fill()
    draw_circle(color, fill_color, radius, x, y)
    t.end_fill()
    
#smile
def draw_smile(color, fill_color, radius, x, y, start_angle, end_angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.width(4)
    t.setheading(270)
    t.circle(radius, 180)
    t.setheading(180)
    t.forward(radius*2)
    t.end_fill()
#total emoji
def draw_smiley():
    t.speed(0)  
    t.bgcolor("blue")  #background color
    t.hideturtle()  

    #face
    draw_circle("yellow", "yellow", 100, 0, -100)

    #eyes
    draw_eye("black","white", 10, -35, 25)
    draw_eye("black","white", 10, 35, 25)

    #smile (color, fill_color, radius, x, y, start_angle, end_angle)
    draw_smile("black", "white", 60, -60, -20, -45, 45)

def draw_afro(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#afro stuff
afro = 8
afro_radius = 60

#draw afro
rancolor = random.random(), random.random(), random.random()
for i in range(afro):
    angle = i * (360 / afro)  
    x = afro_radius * math.cos(math.radians(angle))  
    y = afro_radius * math.sin(math.radians(angle))
    draw_afro(rancolor, 55, x, y)
    


#main smiley function
draw_smiley()

#color cycle
while True:
    t.bgcolor(random.random(), random.random(), random.random())  #changing background color
    time.sleep(.5)



t.update()
t.done()