import random

possibleNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mylist = []

for i in range(10000000):
    mylist.append(random.choice(possibleNums))

n = len(mylist)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swapped = True
    if not swapped:
        break

print(mylist)
