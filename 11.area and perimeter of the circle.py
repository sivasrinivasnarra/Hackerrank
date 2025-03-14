#Write a Program to Calculate Area and Perimeter of Circle.
import math
r=int(input('Enter radius of circle:\n'))
a=math.pi*r**2
p=2*math.pi*r
print(f'The area of the circle is {a:0.2f} and The perimeter of the circle is {p:0.2f}')