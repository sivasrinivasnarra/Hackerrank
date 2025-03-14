#The volume of a sphere with radius r is 4/3 π r3. Input radius and calculate volume of a sphere.
import math
r = int(input())
V = (4 * math.pi * r**3) / 3
print(f"Volume of a sphere with radius {r} is {V:.3f}")
