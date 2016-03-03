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

		# Binds pressing the left arrow key to the turn_left function
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		# Binds pressing the right arrow key to the turn_right function
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

	# Creates a draw function for the Paddle class
	def draw(self):
		# Calls the function move on the canvas
		# Passes 3 parameters: the id of the rectangle, the x we set in the __init__ function
		# We set 0 for the y since the paddle doesn't need to move up or down
		self.canvas.move(self.id, self.x, 0)
	 	# Creates a variable called pos by calling the canvas function coords
		# coords returns the curent x and y coordinates of the parameter you pass it (self.id here)
		# Returns the position in the format [x1, y1, x2, y2] (Top left, top right)
		pos = self.canvas.coords(self.id)
		# Checks to see if the x1 value is equal to 0. If it is then the paddle has hit the left side
		if pos[0] <= 0:
			# If it has then we set x to 0
			self.x = 0
		# Checks to see if the x2 value is equal to the width of the canvas. If it is then the paddle
		# has hit the right side of the screen
		elif pos[2] >= self.canvas_width:
			# If it has then we set x to 0
			self.x = 0

	# A function to turn the paddle left
	def turn_left(self, evt):
		# Sets x to -2
		self.x = -2

	# A function to turn the paddle right
	def turn_right(self, evt):
		# Sets x to 2
		self.x = 2