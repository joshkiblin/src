import Tkinter

top = Tkinter.Tk()
canvas = Tkinter.Canvas(top, width = 500, height = 500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_line(500, 0, 0, 500)
canvas.create_rectangle(100, 100, 400, 400)
top.mainloop()