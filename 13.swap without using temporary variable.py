num1=int(input('Enter First Number:\n'))
num2=int(input('Enter Second Number:\n'))
print(f'Before swapping:\nnum1 is: {num1} and num2 is: {num2}')
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f'After swapping:\nnum1 is: {num1} and num2 is: {num2}')