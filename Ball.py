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
		# Sets x to 0 for the object
		self.x = 0
		# Sets y to -1 for the object
		self.y = -1
		# Set the variable canvas_height to the current height of the canvas
		self.canvas_height = self.canvas.winfo_height()

	# Creates a draw function for the Ball class
	def draw(self):
		# Calls the function move of the canvas.
		# Passes 3 parameters: the id of the oval and the x and y that we set in the initialization
		self.canvas.move(self.id, self.x, self.y)
		# Creates a variable called pos by calling the canvas function coords
		# coords returns the curent x and y coordinates of the parameter you pass it (self.id here)
		# Returns the position in the format [x1, y1, x2, x2] (Top left, top right)
		pos = self.canvas.coords(self.id)
		# Checks to see if y1 (top of ball) is less then or equal to 0
		if pos[1] <= 0:
			# If it is then we set y to 1. This stops the ball from moving up 
			# if it hits the top of the screen and it moves down instead
			self.y = 1
		# Checks to see if y2 is greater than or equal to canvas_height
		if pos[3] >= self.canvas_height:
			# If it is then we set y to -1. This stops the ball from moving down
			# if it hits the bottom of the screen and it moves up instead
			self.y = -1
		