x = raw_input("Hello there, what is your name? ")
print("Welcome " + x + "! Today we will be doing some math, FUN!")


# Pythagorean Theorem

from math import sqrt
print(x + ", please enter the lengths of the legs of a right triangle, a and b. These two numbers will be used to compute the length of the hypotenuse.")
a=float(input("a: "))
b=float(input("b: "))
c=sqrt(a**2 + b**2)
print("The length of the hypotenuse is " + str(c))