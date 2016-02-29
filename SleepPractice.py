import time

t1 = time.time()

for x in range(1, 11):
	print(x)
	time.sleep(1)

t2 = time.time()
print('That took %s seconds to print' % (t2-t1))