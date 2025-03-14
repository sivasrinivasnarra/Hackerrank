#Create a tuple for 2, 4, 5, 6, 2, 3, 4, 4, 7.
#Then write code that does the following:
#(a) Print the values.
#(b) convert the tuple to list.
#(c) Get 4th element of the tuple.
#(d) Get 4th element from last.
#(e) Count 4, the number of times it appears in the tuple.
#(f) Check whether 5 exists within a tuple.
#(g) Find the length of a tuple.
#(h) Unpack a tuple in variables and find sum.
#(i) Create a tuple of one item.
t = (2, 4, 5, 6, 2, 3, 4, 4, 7)
print(f'Tuple: {t}')
l = list(t)
print(f'Convert the tuple to list: {l}')
n = 4
print(f'Get {n}th element of the tuple: {t[n - 1]}')
a = 4
print(f'Get {a}th element from last: {t[-a]}')
b = 4
count = t.count(4)
print(f'Count {4}, the number of times it appears in the tuple: {count}')
o = 5
if o in t:
    print(f'Check whether {o} exists within a tuple: True')
else:
    print(f'Check whether {o} exists within a tuple: false')

print(f'Find the length of a tuple: {len(t)}')
print(f'Unpack a tuple in variables and find sum: {sum(t)}')
i = 2
print(f'Create a tuple of one item: {t[i:i + 1]}')
