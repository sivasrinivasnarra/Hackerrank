#Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food, and then calculate the amount of a 7 percent tip and 15 percent sales tax. Display each of these amounts and the total.
p=int(input("Enter price for meal\n"))
t=0.07*p
s=0.15*p
a=p+t+s
print(f"The tip amount is {t:.1f}\nThe sales tax amount is {s:.1f}\nThe total amount is {a:0.1f}")