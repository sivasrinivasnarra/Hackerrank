#Write a menu-driven code to perform Addition , subtraction , multiplication and division of two complex number.

#Sample I/O
#Enter 1st complex number
#2+3j
#Enter 2nd complex number
#4+5j
#*******
#MENU
#*******
#1.Add
#2.Sub
#3.Mul
#4.Div
#5.Exit
#Enter your choice
#3
#Mul= (-7+22j)
#Enter your choice
#5
#Exiting...
a = complex(input('Enter 1st complex number\n'))
b = complex(input('Enter 2nd complex number\n'))
print('''*******
MENU
*******
1.Add
2.Sub
3.Mul
4.Div
5.Exit''')
while True:
    c = int(input('Enter your choice\n'))
    if c == 1:
        Add = a + b
        print(f'Add= {Add}')
    elif c == 2:
        Sub = a - b
        print(f'Sub= {Sub}')
    elif c == 3:
        Mul = a * b
        print(f'Mul= {Mul}')
    elif c == 4:
        Div = a / b
        print(f'Div= {Div}')
    elif c == 5:
        print('Exiting...')
        break
