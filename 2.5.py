def func(s):
    s1 = s[0:len(s)-1]
    if (len(s) == 1):
        temp2 = []
        temp2.append(s)
        temp2.append('1')
        return ''.join(temp2)
    s2 = s[1:]
    new = []
    flag = True
    temp = []
    for i in range(0,len(s1)):
      if (s1[i] == s2[i]):
        temp.append('1')
      else:
        temp.append('0')
    twin = ''.join(temp)
    temp1 = []
    begin = -1
    end = 1
    temp1.append(s1[0])
    for i in range(0,len(s1)):
        if (twin[i] == '0'):
            end = i
            temp1.append(str(end - begin))
            temp1.append(s2[i])
            begin = end
    temp1.append(str(len(s) - begin - 1) )
    ans = ''.join(temp1)
    return ans
def func_neb(s):
    if (len(s) == 1):
        return s[0]
    s1 = s[1:len(s)] + s[0:1]
    s2 = s[len(s) - 1:len(s)] + s[0:len(s)-1]
    print(s)
    print(s1)
    print(s2)
    temp1 = []
    for i in range(len(s1)):
        temp1.append(str(s1[i] + s2[i]))
        temp1.append(' ')
    ans = ''.join(temp1)
    return ans
s = 'aaabb'
#a = [int (i) for i in input().split()]
a = [1, 2, 3, 4, 5, 6]
print(func_neb(a))

