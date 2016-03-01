import Tkinter

def hello():
	print('Hello there!')

top = Tkinter.Tk()

btn = Tkinter.Button(top, text ="Click me", command = hello)

btn.pack()
top.mainloop()