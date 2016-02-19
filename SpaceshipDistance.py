def spaceship_distance(lightminutes):
	total_distance = 0

	for day in range(1, 29):
		total_distance = total_distance + lightminutes
		print('You have traveled %s lightminutes in %s days' %(lightminutes, day))

spaceship_distance(0.5)