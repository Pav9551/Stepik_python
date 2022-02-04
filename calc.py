# put your python code here
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if (y == 0):
        return "Деление на 0!"
    else:
        return x / y
def f_mod(x, y):
    if (y == 0):
        return "Деление на 0!"
    else:
        return x % y
def f_pow(x, y):
    return pow(x, y)
def f_div(x, y):
    if (y == 0):
        return "Деление на 0!"
    else:
        return x // y
a = float(input())
b = float(input())
choice = input()
if choice == '+':
    print(add(a, b))
elif choice == '-':
    print(subtract(a, b))
elif choice == '*':
    print(multiply(a, b))
elif choice == '/':
    print(divide(a, b))
elif choice == 'mod':
    print(f_mod(a, b))
elif choice == 'pow':
    print(f_pow(a, b))
elif choice == 'div':
    print(f_div(a, b))
else:
    print("Invalid input")