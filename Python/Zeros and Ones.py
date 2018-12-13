# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
import  numpy as n

dimen = tuple(map(int, input().strip().split(" ")))
print(n.zeros(dimen,dtype="int"))
print(n.ones(dimen,dtype="int"))
