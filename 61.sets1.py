#Print out a set containing all the colors from a list which are not present in other list.

#Sample I/O:

#Enter Lists of colors:
#["White", "Black", "Red"]
#["Red", "Green"]

#Result= {'White', 'Black'}
l1=["White", "Black", "Red"]
l2=["Red", "Green"]
s1=set(l1)
s2=set(l2)
print(s1-s2)
