#Write a Program to convert given number of days to a measure of time given in years, weeks and days. For example 375 days is equal to 1 year 1 week and 3 days (ignore leap year )
n=int(input('Enter the number of days \n'))
y=n//365
w=n%365//7
d=n%365%7
print(f'{n} days has {y} years, {w} weeks and {d} days')