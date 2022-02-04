s0 = 4
s1 = 5
for i in range(s0, s1+1):
     print(*range(i, i*s1+1, i), sep='\t')

i = int(input())
s1 = int(input())
j = int(input())
s2 = int(input())
for i in range(1, s1+1):
     for j in range(i, i*s2+1, i):
         print(j, end='\t')
