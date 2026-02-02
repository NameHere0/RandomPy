from random import randint


def func1():
    ls = []
    for i in range(10):
        ls.append(randint(1, 20))
    return ls


def func2(lis):
    newNum = 0
    for i in lis:
        newNum += i
    return newNum


ls = func1()
print(f"list is {ls}")
print(f"its sum is {func2(ls)}")
