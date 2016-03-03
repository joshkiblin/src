# Imports various modules we need
import Tkinter
import random
import time
from Ball import Ball

# Creates a Tkinter object
top = Tkinter.Tk()
# Gives the window the title of 'Game'
top.title('Game')
# Sets the window so that it isn't resizable
top.resizable(0, 0)
# Places the window on top of all other windows
top.wm_attributes("-topmost", 1)

# Creates the canvas and passes it several parameters:
# bd = 0 and highlightthickness = 0 make sure that there isn't a border around the screen
canvas = Tkinter.Canvas(top, width=500, height=400, bd=0, highlightthickness=0)
# Tells the canvas to size itself according to the width and height parameters we pass in line 17
canvas.pack()
# Tells Tkinter to initialize itself
top.update()

# Creates an object named 'ball' of the Ball class that we created in Ball.py
ball = Ball(canvas, 'red')


# Tells the canvas to not loop through the listed command until the user close the window
while 1:
	# Calls the draw function on the ball
	ball.draw()
	# Both of these update the canvas
	top.update_idletasks()
	top.update()
	#Tells the loop to sleep for 1/100th of a second before looping again
	time.sleep(0.01)