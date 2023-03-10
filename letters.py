## This file is the module which contains all the necessay functions to draw the letters
# every letter will be drawn by one function
# it will be called by the main file.



# importing the module turtle and all of its methods
from turtle import *


def letterN ():
    ### the purpose of this function is to draw the first letter, N, which contains three parts:

       # drawing the letter N, first part

    goto(-300,0) # moving the turtle to a start point, located at the left bottom region of the screen
    pendown() # order the turtle to trace
    begin_fill() # filling the future drawing after closing lines
    forward (300) # tracing a straight vertical line from the botton to to top
    circle(10,180) #  drawing half a circle to the left
    forward(300) #tracing back a straight vertical line from the top  to to bottom
    circle(10,180) # drawing the half of circle in order to close the drawing
    end_fill() #filling the drawing after the lines have been closed
    penup() # ordering the turtle to not to draw


        # drawing the letter N, second part

    goto(-315,300) # moving the turtle to th top part so it starts drawing from there
    begin_fill()
    right(157.5)    # in this case, i need to change the dircection of the turtle's head,
                    #setting the angle at -45° on the x axis
                    # so it can draw the diagonal from top left corner to botton right corner.
    pendown()
    forward(330)
    print(position())   # i need this command to get the exact position of the turtle at the end of the execution of the previous command
                        # this helps me to set the right position or angle for next orders.
    print(heading())    #get the angle of the head
    circle(10,180)
    print(position())
    print(heading())
    forward(330)
    circle(10,180)
    end_fill()
    penup()



        # drawing the letter N, third part

    goto(-170,0) # moving the turtle to the bottom  part so it starts drawing from there
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(300)
    circle(10,180)
    forward(300)
    circle(10,180)
    end_fill()
    penup()



def letterI ():
    ### the purpose of this function is to draw the seond letter, I, which contains three parts:

       # drawing the letter I, first part
    
    goto (-130,0) # moving the turtle to the near field next the letter N
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(300)
    circle(10,180)
    forward(300)
    circle(10,180)
    end_fill()
    penup()


def letterZ ():
    ### the purpose of this function is to draw the third letter, Z, which contains three parts:

        # drawing the letter Z, first part

    goto (-90,290) # moving the turtle to the near field next to the top of the letter I
    setheading(0)
    right(90)
    begin_fill()
    pendown()
    forward(175)
    circle(10,180)
    forward(175)
    circle(10,180)
    end_fill()
    penup()


        # drawing the letter Z, second part

    goto (85.00,305.00) # moving the turtle to the right edge of the first part
    setheading(0)       # needed to make calculations of the angle easier
    left(147.5)
    begin_fill()
    pendown()
    forward(350)
    circle(10,180)
    forward(350)
    circle(10,180)
    end_fill()
    penup()


        # drawing the letter Z, third part


    goto (-90.00,10) # moving the turtle to the near field next to the left bottom of the second part
    setheading(0)
    right(90)
    begin_fill()
    pendown()
    forward(175)
    circle(-10,180)
    print(position())  # required to get the position
    forward(175)
    circle(-10,180)
    end_fill()
    penup()


def letterA ():
    ### the purpose of this function is to draw the fourth letter, A, which contains three parts:

        # drawing the letter A, first part

    goto(120.00,0) # moving the turtle next to the right bottom edge of the letter Z
    setheading(0)   # needed to make calculations of the angle easier
    right (25)
    begin_fill()
    pendown()
    forward(330)
    print(position())  # required to get the position for further drawings
    circle(10,180)
    print(position())  
    forward(330)
    circle(10,180)
    end_fill()
    penup()


        #drawing the letter A, second part

    goto(247.92,299.10) # moving the turtle next to the top edge
    setheading(0)   # needed to make calculations of the angle easier
    right(155)
    begin_fill()
    pendown()
    forward(330)
    circle(10,180)
    forward(330)
    circle(10,180)
    end_fill()
    penup()


        # drawing the letter A, third part

    goto(170,150) # moving the turtle to the near field next to the top of the letter I
    setheading(0)
    right(90)
    begin_fill()
    pendown()
    forward(175)
    circle(10,180)
    forward(175)
    circle(10,180)
    end_fill()
    penup()


def letterR ():
    ### the purpose of this function is to draw the fifth and the last letter, R, which contains three parts:

        # drawing the letter R, first part

    goto(440,0) # moving the turtle to the bottom  part, next to the edge, so it starts drawing from there
    setheading(0)  # change the direction of the turtle's head, to make the head towards north
    begin_fill()
    pendown()
    forward(310)
    circle(10,180)
    forward(310)
    circle(10,180)
    end_fill()
    penup()

        # drawing the letter R, second part

    goto(440,310) 
    setheading(0)
    begin_fill()
    pendown()
    backward(20)
    right (90)
    circle(-60,180)
    setheading(0)
    backward(20)
    right (90)
    circle(82.5,180)
    end_fill()
    penup()

        # drawing the letter R, third part

    goto(430.00,160.00) 
    setheading(0)  
    right (155)
    begin_fill()
    pendown()
    forward(180)
    circle(10,180)
    forward(180)
    circle(10,180)
    end_fill()
    penup()





