# https://www.hackerrank.com/challenges/python-mutations/problem
mainString = input()
a, b = [x for x in input().split()]
a1 = int(a)
finalString = mainString[:a1] + b + mainString[a1+1: ]
print(finalString)
