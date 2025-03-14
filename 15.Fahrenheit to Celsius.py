#Write a program to convert Fahrenheit to Celsius.
f=float(input('Enter a temperature in Fahrenheit:\n'))
k=f-32
c=k*5/9
print(f'{f} degree Fahrenheit is equal to {c:0.1f} degree Celsius')