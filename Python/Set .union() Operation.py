# https://www.hackerrank.com/challenges/py-set-union/problem
n1 = int (input())

a= set(map(int,input().strip().split(" ")))
n2 = int (input())

a1= set(map(int,input().strip().split(" ")))

print(len(a.union(a1)))
