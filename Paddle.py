# Imports some modules that we need
import Tkinter
import random
import time

# Creates the class Paddle
class Paddle:
	# An initialization function. User pass two parameters: 'canvas' and 'color'
	def __init__(self, canvas, color):
		# Set the object canvas to the parameter 'canvas' that the user passed
		self.canvas = canvas
		# Creates an rectangle. Uses the color that the user passed
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
		# Moves the rectangle to the middle of the canvas
		self.canvas.move(self.id, 200, 300)
		# Sets x to 0
		self.x = 0
		# Sets canvas_width to the current width of the canvas
		self.canvas_width = self.canvas.winfo_width()

	# Creates a draw function for the Paddle class
	def draw(self):
		pass

	# A function to turn the paddle left
	def turn_left(self, evt):
		# Sets x to -2
		self.x = -2

	# A function to turn the paddle right
	def turn_right(self, evt):
		# Sets x to 2
		self.x = 2