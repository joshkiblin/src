import sys

# Get car A name
print("Please enter the name of the hybrid car")
A = sys.stdin.readline()

# Get car B name
print("Please enter the name of the non hybrid car")
B = sys.stdin.readline()

# Get car A price and store as a float variable
print("Please enter the price of %s" % (A))
PA = sys.stdin.readline()
carA_price = float(PA)

# Get car B price and store as a float variable
print("Please enter the price of %s" % (B))
PB = sys.stdin.readline()
carB_price = float(PB)

# Subtracts the price of car B price from car A price and store as retail cost difference variable
RCD = carA_price - carB_price

# Get average gas price variable and store as average price variable
print("Please enter the average price of gasoline per gallon for your area")
GP = sys.stdin.readline()
gas_price = float(GP)

# Get combined mpg for car A and store as a variable
print ("please enter the combined mpg for %s" % (A))
tempMPGA = sys.stdin.readline()
mpgA = float(tempMPGA)

# Get combined mpg for car B and store as a variable
print ("please enter the combined mpg for %s" % (B))
tempMPGB = sys.stdin.readline()
mpgB = float(tempMPGB)

# Calculate average cost/mile for car A and store as variable ACM
ACM = gas_price / mpgA

# Calculate average cost/mile for car B and store as variable BCM
BCM = gas_price / mpgB

# Calculate cost/mile difference BCM minus ACM and store as variable CMD
CMD = BCM - ACM

# Calculate miles to break even point through retail cost difference/CMD and store as BEPM
BEPM = RCD / CMD
BEPMi = int(BEPM)

# Return results to user with nice message containing BEPM on the screen
print("In order to get your money back driving a %s you have to drive %s miles" % (A, BEPMi))