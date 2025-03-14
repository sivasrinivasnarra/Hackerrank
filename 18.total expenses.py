#While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than and equal to 100. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses. Using simple if statement.
p=int(input("Enter the price:\n"))
q=int(input("Enter the quantity:\n"))
if q>=100:
    print(f"Total amount to be paid: {0.9*p*q:.1f}")
else:
    print(f"Total amount to be paid: {p*q:.1f}")