import pytest
import math
def my_function_1_10(A,B,H):
    if (H < A):
        return "Недосып"
    if (H > B):
        return "Пересып"
    if (H >= A) and (H <= B):
        return "Это нормально"
def test_func():
    a = [6, 7, 7]
    b = [10, 9, 9]
    c = [8, 10, 2]
    d = ["Это нормально", "Пересып","Недосып"]
    res = list(zip(a, b, c))#Sample Input
    ans = d #Sample Output
    assert list(map(lambda y: my_function_1_10(*y), res)) == ans
# C:\Users\pavel\PycharmProjects\pythonStepik>pytest -v