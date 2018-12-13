# https://www.hackerrank.com/challenges/symmetric-difference/problem
n1 = int(input())

a = set(map(int,input().strip().split(" ")))

n2= int(input())

b = set(map(int,input().strip().split(" ")))

res1 = sorted(a.difference(b))

res2 = sorted(b.difference(a))
list1 = []
for item in res1:
    list1.append(item)
for item1 in res2:
    list1.append(item1)
list12 = sorted(list1)

for it in list12:
    print(it)
