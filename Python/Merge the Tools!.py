# https://www.hackerrank.com/challenges/merge-the-tools/problem

from collections import OrderedDict
z= input()

k = int(input())
a = int(len(z)/k)
store = []
for i in range(a):
    temp = z[i * k : (i+1) * k ]
    store.append(temp)

for items in store:
    print("".join(OrderedDict.fromkeys(items)))
