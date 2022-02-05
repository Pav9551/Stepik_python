import pytest
def my_function_1_10_1(A,B,H):
    if (H < A):
        return "Недосып"
    if (H > B):
        return "Пересып"
    if (H >= A) and (H <= B):
        return "Это нормально"

def test_func_1():
    a = [6, 7, 7]
    b = [10, 9, 9]
    c = [8, 10, 2]
    d = ["Это нормально", "Пересып","Недосып"]
    res = list(zip(a, b, c))#Sample Input
    ans = d #Sample Output
    assert list(map(lambda y: my_function_1_10_1(*y), res)) == ans
def func(str_):

    print(str_)
    print(str_.split(" "))
    s = str_.split(" ")
    s.sort()
    s.append(1000)#костыль
    print(s)
    temp1 = []
    cnt = 1
    cnt_last = 0
    #print(s)
    for i in range(len(s)-1):
        if s[i] != s[i + 1]:
            #print(s[i] + str(cnt), end='')
            if (cnt>1):
                temp1.append(str(s[i]))
                temp1.append(' ')
            cnt = 1
        else:
            cnt += 1
        #print(s[i] + str(cnt))

    ans = ''.join(temp1[0:len(temp1)-1])#костыль
    print()
    return ans

def test_func_2():
    in1 = "4 8 0 3 4 2 0 3"
    out1 ="0 3 4"
    in2 = "10"
    out2 = ""
    in3 = "1 1 2 2 3 3"
    out3 = "1 2 3"
    in4 = "1 1 1 1 1 2 2 2"
    out4 = "1 2"

    in_ = [in1,in2,in3,in4]
    out_= [out1,out2,out3,out4]

    print(in_)
    print(out_)
    assert list(map(lambda y: func(y), in_)) == out_
a="4 8 0 3 4 2 0 3"
a="1 1 2 2 3 3 3"
#print(a)
print(func(a))

