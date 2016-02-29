import copy

name1 = 'Nathaniel'
print(name1)

name2 = copy.copy(name1)
print(name2)

names = ['Billy', 'Smith', 'Fred']
print(names)
more_names = copy.copy(names)
print(more_names)

names[0] = 'Bill'
print(names)
print(more_names)