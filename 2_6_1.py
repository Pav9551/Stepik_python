k = 4
if k == 1:
    print(f'1', end='')
if k == 2:
    print(f'1 2', end='')

if k > 2:
    for i in range(k):
        if (k == 0):
            break
        for j in range(i):
            k = k - 1
            print(f'{i} ', end='')
            if (k == 0):
                break
