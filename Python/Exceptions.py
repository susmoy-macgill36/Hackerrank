# https://www.hackerrank.com/challenges/exceptions/problem
n = int(input())

for i  in range(n):

    a, b = [x for x in input().split()]
    try:
         x= int(a)//int(b)
         print(x)
    except Exception as e:
        print ("Error Code:", e)
