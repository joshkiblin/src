# Get car A name
a = raw_input('Please enter the name of the hybrid car: ')

# Get car B name
b = raw_input('Please enter the name of the non-hybrid car: ')

# Get car A price
pa = input('Please enter the price of the hybrid car: ')

# Get car B price
pb = input('Please enter the price of the non-hybrid car: ')

# Subtract price of car b from car a to get the retail cost difference
RCD = pa - pb

# Get the price of gas
gp = input('Please enter the average price of gasoline per gallon for your area: ')

# Get the MPG for car A
mpgA = input('Please enter the combined mpg for %s: ' % (a))

# Get the MPG for car B
mpgB = input('Please enter the combined mpg for %s: ' % (b))

# Calculate average cost/mile for car A and store as variable ACM
ACM = gp / mpgA

# Calculate average cost/mile for car B and store as variable BCM
BCM = gp / mpgB

# Calculate cost/mile difference BCM minus ACM and store as variable CMD
CMD = BCM - ACM

# Calculate miles to break even point through retail cost difference/CMD and store as BEPM
BEPM = RCD / CMD
BEPMi = int(BEPM)

# Return results to user with nice message containing BEPM on the screen
print("In order to get your money back driving a %s you have to drive %s miles" % (a, BEPMi))