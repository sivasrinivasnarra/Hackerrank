#Write a program that asks the user to enter a positive number and then prints out the square root of that number to 2 decimal places.
import math
n=int(input("Enter a positive number:\n"))
print(f"To 2 decimal place, {n} square root is {math.sqrt(n):0.2f}")