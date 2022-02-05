#a = [int(i) for i in input().split()]
a = [5,8,2,7,8,8,2,4]
x = int(input())

for i in range(len(a)):
    if (a[i] == x):
        print(f'{i} ', end='')