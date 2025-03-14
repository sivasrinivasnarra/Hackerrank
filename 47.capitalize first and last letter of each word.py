s=input("Enter a string:\n")
l=s.split()
k=[]
for i in l:
    if len(i)==1:
        k.append(i.upper())
    else:
        k.append(i[0].upper()+i[1:-1]+i[-1].upper())
m=' '.join(k)
print(m)