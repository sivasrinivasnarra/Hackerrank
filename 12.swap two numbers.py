#Write a program to swap two numbers
num1=int(input("num1"))
num2=int(input("num2"))
print(f'Before swapping:\nnum1 is: {num1} and num2 is: {num2}')
t=num1
num1=num2
num2=t
print(f'After swapping:\nnum1 is: {num1} and num2 is: {num2}')