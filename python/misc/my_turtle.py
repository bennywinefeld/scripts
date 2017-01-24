import turtle
import tkSimpleDialog
j = turtle.Turtle()

for i in range(3):
    name = tkSimpleDialog.askstring("name","what's your name?")
    radius = tkSimpleDialog.askinteger("yasha","Enter radius")
    print "radius=",radius 
    print "Hi,",name
    j.circle(radius)