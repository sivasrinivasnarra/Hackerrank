r = int(input('Enter the range:\n'))
p = [2]
for i in range(3, r + 1):
    for j in range(2, i):
        if i % j != 0:
            if j == i - 1:
                p.append(i)

        else:
            break
print(f'Prime numbers are: {p}')