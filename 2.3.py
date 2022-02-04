a1 = 7
a2 = 10
b1 = 5
b2 = 6
print(f'{""}\t', end='')
for k in range(b1, b2+1):
    print(f'{k}\t', end='')
print('')
for i in range(a1, a2+1):
    for k in range(b1, b2+1):
        if (k == b1): print(f'{i}\t', end='')
        print(f'{i * k}\t', end='')
    print('')

