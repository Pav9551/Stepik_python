# put your python code here

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
s = 'aaabb'
print(func(s))

