import time

# print(time.time())

def many_numbers(max):
	t1 = time.time()
	for x in range(0, max):
		print(x)
	t2 = time.time()
	print('It took %s seconds to print 0 through %s!' % (t2-t1, max - 1))

# many_numbers(1235)

print(time.asctime())

# year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight savings time

t = (2010, 2, 12, 12, 8, 0, 0, 0, 0)
print(time.asctime(t))