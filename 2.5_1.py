a = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6 , 4, 5, 6]
a = [4, 8, 0, 3, 4, 2, 0, 3]
def func_neb(s):
    s.sort()
    #print(s)
    temp1 = []
    cnt = 0
    cnt_last = 0
    #print(s)
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:  # сравниваем символ по текущему индексу со следующим
            cnt += 1  # если символы одинаковые, то увеличиваем счетчик
            #print(f'Пара {s[i]} {cnt}\t', end='')
        else:
            if (cnt > 1):
                temp1.append(str(s[i]))
                temp1.append(' ')
            cnt_last = cnt
            cnt = 1  # счетчик текущего символа на единице
            #print(f'-- {cnt}\t', end='')
            #print()

    ans = ''.join(temp1)
    return ans
#a = [int (i) for i in input().split()]
print(func_neb(a))