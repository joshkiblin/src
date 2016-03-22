from fractions import Fraction

a = 3
print(a + 1)
a = 5
print(a + 1)

print(type(3))
print(type(3.5))
print(type(3.0))

print(int(3.8))
print(int(3.0))

print(float(3))

f = Fraction(3, 4)
print f

print(f + 1 + 1.5)

print(f + 1 + Fraction(1, 4))

a = 2 + 3j
print(type(a))

a = complex(2, 3)
print(a)

b = 3 + 3j
print (a + b)
print (a - b)

print (a * b)
print (a / b)

z = 2 + 3j
print(z.real)
print(z.imag)

print (z.conjugate())

print (z.real ** 2 + z.imag ** 2) ** 0.5

print (abs(z))