#Write a program to find the roots of Qudratic Equation.

#The mathematical representation of a Quadratic Equation is ax²+bx+c = 0. A Quadratic Equation can have two roots, and they depend entirely upon the discriminant.

#If discriminant > 0, then Two Distinct Real Roots exists for this equation

a=int(input("Enter a Value:\n"))
b=int(input("Enter b Value:\n"))
c=int(input("Enter c Value:\n"))
d=(b**2)-4*a*c
if d<0:
    print("Roots are imaginary")
else:
    if d==0:
        print("Roots are Real and Equal")
        print(f"Root1 = {(-b/(2*a)):.2f} and Root2 = {(-b/(2*a)):.2f}")
    else:
        print("Roots are Real and Distinct")
        print(f"Root1 = {((-b+d**0.5)/(2*a)):.2f} and Root2 = {((-b-d**0.5)/(2*a)):.2f}")