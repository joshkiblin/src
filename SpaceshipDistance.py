def spaceship_distance(lightminutes):
	total_distance = 0
	for week in range(1, 53):
		total_distance = total_distance + lightminutes
		print('Week %s = %s lightminutes' % (week, total_distance))

spaceship_distance(2)
