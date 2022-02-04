import pytest
import math
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
def my_function_1_10_2(A):
    if (((A % 4 == 0) and (A % 100 != 0)) or (A % 400 == 0)):
        return "Високосный"
    else:
        return "Обычный"
def test_func_2():
    a = [2000, 2100, 1988, 1992, 1996]
    d = ["Високосный","Обычный","Високосный","Високосный","Високосный"]
    res = a #Sample Input
    ans = d #Sample Output
    assert list(map(lambda y: my_function_1_10_2(y), res)) == ans

# C:\Users\pavel\PycharmProjects\pythonStepik>pytest -v