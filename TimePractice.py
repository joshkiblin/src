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

t = (2013, 11, 13, 3, 12, 0, 4, 0, 0)
print(time.asctime(t))

t = time.localtime()

year = t[0]
month = t[1]

print('We are in month %s of %s' % (month, year))