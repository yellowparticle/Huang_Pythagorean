print ("Please enter the lengths of three legs of a triangle, a, b, and c.")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
if (a+b<c):
    print("The lengths entered do not make a right triangle!")
if (a**2 + b**2 == c**2):
    print("The lengths entered make a right triangle!")
if (a**2 + b**2 < c**2):
    print("The lengths entered make an obtuse triangle!")
if (a**2 + b**2 > c**2):
    print("The lengths entered make an acute triangle!")