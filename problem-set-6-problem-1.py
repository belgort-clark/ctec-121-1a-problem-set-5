# CTEC 121
# YOUR NAME
# Module 6 / Problem Set 4
# Problem 1 (25 points)

'''
SNOWMAN SPECIFICATIONS
=======================

Using the starter code provided, write a Python program that will create a snowman.
Be sure to change YOUR NAME to your first and last name

- The snowman must contain 3 circles for the body.
- The snowman must have two eyes on its face drawn with circles.
- The snowman must have a nose made out of a tirangle and it must be colored orange.
- The snowman must have a hat made out of a rectangle and a line (a top hat).
- The hat must be filled with the color black.
- The snowman must have two arms drawn using lines.

'''

import graphics


def snowman():
    # create the graphics window
    win = graphics.GraphWin('Problem 1 - Snowman', 800, 800)

    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circle3

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    # draw two arms that connect to the body of the snowman
    # name the line objects leftArm and rightArm

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()
