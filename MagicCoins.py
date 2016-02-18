found_coins = 20
magic_coins = 7
stolen_coins = 3
coins = found_coins

for day in range(1, 366):
	coins = coins + magic_coins - stolen_coins
	print('Day %s = %s' % (day, coins))