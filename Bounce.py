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

canvas = Tkinter.Canvas(top, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
top.update()

ball = Ball(canvas, 'red')
canvas.mainloop()