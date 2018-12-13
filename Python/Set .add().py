# https://www.hackerrank.com/challenges/py-set-add/problem

n1 = int(input())
set1 = {""}

set1.remove("")
for i in range(n1):
    set1.add(input())


print(len(set1))
