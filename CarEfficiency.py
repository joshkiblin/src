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

