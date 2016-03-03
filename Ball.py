# Import modules that we need
import Tkinter
import random
import time

#Creates the class 'Ball'
class Ball:
	# An initialization function. User pass three parameters: 'canvas', 'paddle' and 'color'
	def __init__(self, canvas, paddle, color):
		# Set the object canvas to the parameter 'canvas' that the user passed
		self.canvas = canvas

		# Sets the object paddle to the parameter 'paddle' that the user passed
		self.paddle = paddle

		# Creates an oval. Uses the color that the user passed
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		# Moves the oval to the middle of the canvas
		self.canvas.move(self.id, 245, 100)
		
		# Creates a list of 6 potential starts
		starts = [-3, -2, -1, 1, 2, 3]
		# Uses random to shuffle to order in starts
		random.shuffle(starts)
		# Chooses the new first item in starts
		self.x = starts[0]
		# Selts y to -3
		self.y = -3
		
		# Set the variable canvas_height to the current height of the canvas
		self.canvas_height = self.canvas.winfo_height()
		# Set the variable canvas_width to the current width of the canvas
		self.canvas_width = self.canvas.winfo_width()

	# Creates a function hit_paddle. Passes the parameter pos
	def hit_paddle(self, pos):

		## Creates a variable called paddle_pos by calling the canvas function coords
		# coords returns the curent x and y coordinates of the parameter you pass it (self.paddle.id here)
		# Returns the position in the format [x1, y1, x2, y2] (Top left, top right)
		paddle_pos = self.canvas.coords(self.paddle.id)

		# Checks to see if the x2 of the pos that is passed is greater than or equal to the x1 of the 
		# paddle AND if the x1 of the pos that is passed is less than of equal to the x2 of the paddle
		# This means that we are looking to see if the position of the ball is completely between the
		# left side of the paddle and the right side of the paddle
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			# Checks to see if the y2 of the pos that is passed is greater than or equal to the y1 of the
			# paddle AND if the y2 of the pos that is passed is less than or equal to the y2 of the paddle
			# This means that we are looking to see if the postion of the ball is above the paddle
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				# If both of the above if statements are true then we return true for the function
				return True
		# If one or both aren't true then we return false
		return False

	# Creates a draw function for the Ball class
	def draw(self):
		
		# Calls the function move of the canvas.
		# Passes 3 parameters: the id of the oval and the x and y that we set in the initialization
		self.canvas.move(self.id, self.x, self.y)
		
		# Creates a variable called pos by calling the canvas function coords
		# coords returns the curent x and y coordinates of the parameter you pass it (self.id here)
		# Returns the position in the format [x1, y1, x2, y2] (Top left, top right)
		pos = self.canvas.coords(self.id)
		
		# Checks to see if y1 (top of ball) is less than or equal to 0
		# This would mean the bottom of the ball has hit the top of the screen
		if pos[1] <= 0:
			# If it has then we set y to 1. This stops the ball from moving up 
			# now that it has hit the top of the screen and it moves down instead
			self.y = 3
		
		# Checks to see if y2 (bottom of ball) is greater than or equal to canvas_height
		# This would mean the the bottom of the ball has hit the bottom of the screen
		if pos[3] >= self.canvas_height:
			# If it has then we set y to -1. This stops the ball from moving down
			# now that it has hit the bottom of the screen and it moves up instead
			self.y = -3
		
		# Checks to see if the function hit_paddle returns True
		if self.hit_paddle(pos) == True:
			# If it returns true then we set y to -3
			self.y = -3
		
		# Checks to see if x1 (top left of ball) is less than or equal to 0
		# This would mean that the left side of the ball has hit the left side of the screen
		if pos[0] <= 0:
			# If it has then we set x to 3 which would now make it move right. This stops the ball
			# from moving left now that it has hit the left side of the screen.
			self.x = 3
		
		# Checks to see if x2 (the bottom right of the ball) is greater than or equal to canvas_width
		# This would mean that the right side of the ball has hit the right side of the screen
		if pos[2] >= self.canvas_width:
			# If it has then we set x to -3 which would now make it move left. This stops the ball
			# from moving right now that it has hit the right side of the screen.
			self.x = -3