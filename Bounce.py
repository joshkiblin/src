import Tkinter
import random
import time

top = Tkinter.Tk()
top.title('Game')
top.resizable(0, 0)
top.wm_attributes("-topmost", 1)
canvas = Tkinter.Canvas(top, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
top.update()
top.mainloop()