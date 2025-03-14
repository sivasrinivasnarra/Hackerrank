#(a) Print out the total number of items in the list.
#(b) Print out the fourth item in the list.
#(c) Print out the last three items in the list.
#(d) Print out all the items in the list except the first two.
#(e) Print out the list in reverse order.
#(f) Print out the largest and smallest values in the list.
#(g) Sort the list and print out the list after sorting.
#(h) Delete the first item from the (now sorted) list and print out the new list.
#(i) Append the value -500 to the end of the list and print out the new list.
a=eval(input('Enter a list of integers:\n'))
print(f'List: {a}')
print(f'The total number of items in the list: {len(a)}')
print(f'The fourth item in the list: {a[3]}')
print(f'The last three items in the list: {a[len(a)-3::]}')
print(f'All the items in the list except the first two: {a[2::]}')
print(f'The list in reverse order: {a[-1::-1]}')
print(f'The largest and smallest values in the list: {max(a)} {min(a)}')
a.sort()
print(f'The list after sorting: {a}')
del a[0]
print(f'List after deleting first item: {a}')
a.append(-500)
print(f'List after appending: {a}')