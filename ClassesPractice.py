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
	def eat_leaves(self):
		print('eating leaves')

reginald = Giraffes()

reginald.move()
reginald.eat_leaves()
reginald.breathe()