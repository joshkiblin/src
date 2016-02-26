import math

# Welcomes the user
print('')
print('Welcome to the Amazing Atomic Emission application!')
print('This program will use the E value you measured and recorded in')
print('scientific notation in order to determine the relative energy of')
print('the energy level transition along with reporting the wavelength')
print('in meters and frequency in Hertz of the energy emission.')
print('')

# Prompts the user for the significand, the initial number part of the scientific notation.
# Stores the value as a variable named significand.
significand = input('Please input the significand value (the number at the beginning) of your E value and press return: ')

# Prompts the user for the exponential power of the scientific notation
# Stores the value as a variable named exponent
exponent = input('Please input the exponential power of your E value (the number 10 is raised to) and press return: ')

# Uses the significand and exponent inputted by the user to assemble a value for E.
E = significand * (10**exponent)

# Declares Plank's Constant as h
h = 6.62606876 * (10**(-34))

# Declates the speed of light in m/s as C
C = 299792458.0