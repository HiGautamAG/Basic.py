import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)

n= 39
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h/360, 1.0, 1.0)
    h+=1/n
    t.color(c)
    t.left(145)
    
    for j in range(5):
        t.forward(360)
        t.right(150)