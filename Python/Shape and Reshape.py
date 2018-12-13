# https://www.hackerrank.com/challenges/np-shape-reshape/problem
import  numpy as n

b= n.array(list(map(int, input().split())))
print(n.reshape(b,(3,3)))
