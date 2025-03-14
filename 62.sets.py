#Write a Python program to check a given set has no elements in common with other given set.

#Sample I/O:
#Enter Sets:
#{1,2,3}
#{4,5,6}
#{3}
#{1, 2, 3} set has no elements in common with {4, 5, 6} set:
#True
#{1, 2, 3} set has no elements in common with {3} set:
#False
a=eval(input('Enter Sets:\n'))
b=eval(input())
c=eval(input())
if len(a.intersection(b))==0:
    print(f'{a} set has no elements in common with {b} set:\nTrue')
else:
          print(f'{a} set has no elements in common with {b} set:\nFalse')
if len(a.intersection(c))==0:
    print(f'{a} set has no elements in common with {c} set:\nTrue')
else:
          print(f'{a} set has no elements in common with {c} set:\nFalse')
