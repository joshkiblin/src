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

# Divides E by h and stores the value as v. v represents the frequency or cycles per
# second of the energy wave emitted.
v = E / h

# Divides C by v to determine the wavelength of a single cycle in meters and stores as wavelength
wavelength = C / v

# Declaration of Visable light and UV limits for wavelength
# Used to determine whether the energy emitted is IR, Visable Light or UV
visLimit = 7 * 10**(-7)
uvLimit = 38 * 10**(-8)

# Run comparision and set variables based on results
if wavelength > visLimit:
	type = 'low'
	range = 'infrared'
elif visLimit > wavelength and wavelength > uvLimit:
	type = 'medium'
	range = 'visable light'
else:
	type = 'high'
	range = 'ultra violet'

# Return the data to the user
print('')
print('The frequency of the energy wave emitted was %s Hertz (cycles/sec)' % (v))
print('')
print('The length of each wave was %s meters' % (wavelength))
print('')
print('So based on the information above, it is determined')
print('that the energy emitted was %s level in the %s range of the specturm' % (type, range))
print('')
print('Thanks for using the Amazing Atomic Emission application!')