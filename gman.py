import random

blist = [random.randint(-100, 100) for _ in range(10)]
n = len(blist)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if blist[j] > blist[j + 1]:
            blist[j], blist[j + 1] = blist[j + 1], blist[j]

print(blist)