# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n1 = int (input())

a= set(map(int,input().strip().split(" ")))
n2 = int (input())

a1= set(map(int,input().strip().split(" ")))

print(len(a.intersection(a1)))
