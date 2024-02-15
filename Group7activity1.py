import turtle as t # Importing the turtle module from the python library
'''
This is a program that aims to boost the proficiency in python, using turtle.

    There are various functions in this assigment:
        SetPos function, which takes x and y for parameters, and moves the turtle to those co-ordinates.
        hexagon function, which takes turta, hexa_color and border_color as parameters and draws a hexagon.
        circle function, which takes turta, circle_color and border_color as parameters and draws a circle.
        square function, which takes turta, square_color and border_color as parameters and draws a square.
        main function, which helps orchestrate the entire code, by sending the initial input color parameters, and calling SetPos with the pattern function.


    In accordance with the provided assignment:
        The code takes parameters from the user for the colors, and sends the arguements to the actual functions as we call them to draw.

    This program uses the concept of incremental development which refers to using multiple functions which have various instructions 
    within them and take multiple parameters those functions are later called from a singular main function. 
    This keeps our code easy-to-read, organized and simplifies the process of development.

    Overall, this was a fun experience and it helped all of us improve our python coding skills and advanced our understanding
    of the python library, along with practicing already basic concepts provided to us in the GCIS 123 Class.

Group 7
    1 - Yousef Al Salman, ysa1392
    2 - Ahmed Nayebkhil, asn7942
    3 - Omar Al Gendi, oae5541
'''



#Importing turtle as t for ease of usage and calling.


#The set position function, this function basically lifts the pen up as to avoid drawing, then goes to a certain coordinate which is assigned.
def setPos(turta, x,y):
    turta.up()
    turta.goto(x,y)


#Hexagon function, draws a hexagon. Can have a custom color and border color.
def Hexagon(turta, hexa_color, border_color):

    #initilization, pen down.
    turta.down()

    #Colors selection
    turta.color(border_color)
    turta.fillcolor(hexa_color)

    #Begin Filling
    turta.begin_fill()

    # Drawing the hexagon
    turta.forward(50)
    turta.right(300)
    turta.forward(50)
    turta.right(300)
    turta.forward(50)
    turta.right(300)
    turta.forward(50)
    turta.right(300)
    turta.forward(50)
    turta.right(300)
    turta.forward(50)
    turta.right(300)

    #End fill
    t.end_fill()

    #Pen up, closing.
    t.penup()

#The circle function which takes a custom color and border color.
def circle(turta,circle_color,border_color):
    
    #initilization
    turta.down()

    #Colors selection
    turta.color(border_color)
    turta.fillcolor(circle_color)

    #Begin filling
    turta.begin_fill()

    #Circle
    turta.circle(45)

    #End filling
    turta.end_fill()

    #Pen up, ending.
    turta.penup()

#The square function, which takes custom colors and border color.
def square(turta,square_color,border_color):

    #Pen initilization
    turta.down()

    #Color selection
    turta.color(border_color)
    turta.fillcolor(square_color)

    #Begin filling
    turta.begin_fill()

    #Square Drawing
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)

    #End filling
    turta.end_fill()

    #Drawing complete, pen up.
    turta.up()


#Pattern function which takes the colors for each shape and border color and draws the three shapes with some distance between them.
def pattern(turta, hexa_color, circle_color, square_color, border_color):

    # This calls the hexagon function, with certain parameters to draw it.
    Hexagon(turta, hexa_color, border_color)
    turta.forward(140)
    # This calls the circle function, with certain parameters to draw it.
    circle(turta, circle_color, border_color)
    turta.forward(80)
    # This calls the square function with certain parameters to draw it.
    square(turta, square_color, border_color)



# The main function which will draw our pattern and position it.
def main():
    # within the main function, we will take inputs for our functions parameters, such as hexa_color, circle_color, square_color and border_color
    hexa_color = input("Enter the color of the hexagon: ")
    circle_color = input("Enter the color of the circle: ")
    square_color = input("Enter the color of the square: ")
    border_color = input("Enter the color of the border: ")

    # We make use of the position helper function by moving the position of the turtle before calling the pattern.
    setPos(t, -250,90)
    pattern(t, hexa_color, circle_color, square_color, border_color)
    setPos(t, -200,-50)
    pattern(t, hexa_color, circle_color, square_color, border_color)
    setPos(t, -150,-190)
    pattern(t, hexa_color, circle_color, square_color, border_color)
    t.exitonclick() # To keep the drawing on the screen until the user clicks the exit button


# Calling the main function, which is the brain of our code.
main()


