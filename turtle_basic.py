#importing libraries
from turtle import *
import math
ht()
#for easier use
def draw(side,angle):
    forward(side)
    left(angle)
#for drawing square    
def square (side1,colour1="black",colour2="black"):
    color(colour1,colour2)
    begin_fill()
    side=1
    while side<=4:
        draw(side1,90)
        side+=1
    end_fill()
    done()
#for drawing rectangle       
def rectangle(side1,side2,colour1="black",colour2="black"):
    color(colour1,colour2)
    begin_fill()
    side=1
    while side<=2:
        draw(side1,90)
        draw(side2,90)
        side+=1
    end_fill()
    pendown()
    done()
#for drawing triangle
def triangle(side1,side2=0,angle1=120,angle2=60,colour1="black",colour2="black"):
    angle1=180-angle1
    if side2==0:
        side2=side1
    color(colour1,colour2)
    begin_fill()
    draw(side1,angle1)
    draw(side2,angle2)
    end_fill()
    pendown()
    done()
#go to a position     
def pos(x,y):
    penup()
    goto(x,y) 
    pendown()
#draw star    
def star(length,colour1="black",colour2="black"):
    color(colour1,colour2)  
    begin_fill()
    side=1
    while side<=4:
        side=side+1
        draw(length,144)    
    end_fill()
    done()
#draw polystars    
def polystar(length,sides,angles,colour1="black",colour2="black"):
    color(colour1,colour2)  
    begin_fill()
    side=1
    while side<=sides:
        side=side+1
        draw(length,angles)    
    end_fill()
    done() 
#draw lines       
def line(x,y,a,b):
    penup()
    goto(x,y)
    pendown()
    goto(a,b)
    done()
#draw parabola    
def parabola(x:int,a:int):
    penup()
    goto(x,a*x*x)
    X=x
    pendown()
    while x>=0:
        x-=1
        y=a*x*x
        goto(x,y)
        if(x==0):
            goto(0,0)        
    while x!=X:
        x+=1
        y=a*x*x
        goto(-x,y)
    done()
#draw curve    
def curve(length,angle):
    while length!=0: 
        left(angle/100)
        forward(1)
        length-=1
    done()
#draw different types of polygon of same size
def polygon(length,sides):
    circle(length,steps=sides)
    done()
#to draw circle with different border colur    
def colourcircle(radius,colour1="black",colour2="black"):
    color(colour1,colour2)
    begin_fill()    
    circle(radius)
    end_fill()    
