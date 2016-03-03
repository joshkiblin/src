# Import modules that we need
import Tkinter
import random
import time

#Creates the class 'Ball'
class Ball:
	# An initialization function. User pass two parameters: 'canvas' and 'color'
	def __init__(self, canvas, color):
		# Set the object canvas to the parameter 'canvas' that the user passed
		self.canvas = canvas
		# Creates an oval. Uses the color that the user passed
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		# Moves the oval to the middle of the canvas
		self.canvas.move(self.id, 245, 100)

	def draw(self):
		pass
		