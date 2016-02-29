import random
num = random.randint(1, 100)
print(num)

while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i > 100 or i < 1:
		print("You guessed a number that wasn't within the range")
	elif i == num:
		print("You're right!")
		break
	elif i > num:
		print('Too high')
	elif i < num:
		print('Too low')

names = ['Billy', 'Smith', 'Fred']
print(random.choice(names))
random.shuffle(names)
print(names)