import pickle

game_data = {
	'player_position' : 'N23 E45',
	'pockets' : ['keys', 'knife', 'apple'],
	'backpack' : ['sleeping bag', 'clothes', 'food']
}

save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)