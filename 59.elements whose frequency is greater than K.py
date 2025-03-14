l = input("Input List:\n")
k = int(input("Input K:\n"))
l = l.strip('[]').replace("'", "").split(',')
l = [int(x) for x in l]
from collections import Counter

a = Counter(l)
m = []
for element, count in a.items():
    if count > k:
        m.append(element)
print(f"Output : {m}")
