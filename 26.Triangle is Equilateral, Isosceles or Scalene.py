x = int(input("X =\n"))
y = int(input("Y =\n"))
z = int(input("Z =\n"))
if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
