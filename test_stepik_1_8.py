import pytest
import math
def my_function_1_8(X,H,M):
    XX = X + H*60 + M
    H1 = XX//60
    M1 = XX - H1*60
    return H1,M1
def test_func():
    a = [480, 475]
    b = [1, 1]
    c = [2, 55]
    d = [9, 9]
    e = [2, 50]
    res = list(zip(a, b, c))#Sample Input
    ans = list(zip(d, e))#Sample Output
    assert list(map(lambda y: my_function_1_8(*y), res)) == ans