#Write a ‘Python’ program to accept list of elements and key element from user and perform linear search, print element found along with its position or element Not found.

l = list(map(int,input("Enter the list:\n").strip().split()))
k=int(input("Enter Key: \n"))
if k in l:
    position = l.index(k) + 1
    print(f"Element {k} FOUND at position {position}")
else:
    print(f"Element {k} NOT FOUND")