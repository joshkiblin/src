import turtle

t = turtle.Pen()

# t.forward(150)
# t.left(90)
# t.forward(150)
# t.left(90)
# t.forward(150)
# t.left(90)
# t.forward(150)

# for x in range(1,56):
#	t.forward(200)
#	t.left(92)

for x in range(1, 19):
	t.forward(100)
	if x % 2 == 0:
		t.left(175)
	else:
		t.left(225)