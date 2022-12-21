# This program is intended to draw my name using the language Python and the module turtle
# this version is used with one module which contains functions
# every function consists in drawing only one letter.



# importing the module turtle and all of its methods
from turtle import *


# importing the module ' letters ', so that the functions can be called.

from letters import letterN, letterI, letterZ, letterA, letterR

#defining the screen as an object
screen=Screen()
screen.bgcolor("white")
screen.title("Writing My Name, another edition")

# defining the turtle as the object which makes the drawing
color("black")
speed(0)
mode("logo") # to make the turtle head to the north, and the postitve angles for counterclockwise rotation
penup()
hideturtle() # it is optinal, just to hide the object to make better animation


    
    




