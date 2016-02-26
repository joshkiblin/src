class Things:
	pass

class Inanimate(Things):
	pass

class Animate(Things):
	pass

class Sidewalks(Inanimate):
	pass

class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')

class Mammals(Animals):
	def feed_young_with_milk(self):
		print ('feeding young')

class Giraffes(Mammals):
	def __init__(self, spots):
		self.giraffes_spots = spots
	def eat_leaves(self):
		print('eating leaves')
	def find_food(self):
		self.move()
		print("I've found food!")
		self.eat_food()

reginald = Giraffes(123)

reginald.move()
reginald.eat_leaves()
reginald.breathe()
reginald.find_food()
print(reginald.giraffes_spots)