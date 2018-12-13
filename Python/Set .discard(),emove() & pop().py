# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n1 = int (input())

s1= set(map(int,input().strip().split(" ")))
n2 = int (input())

for i in  range(n2):
    a= input().strip().split(" ")

    if a[0] == "pop":
        s1.pop()
    elif a[0] == "remove":
        s1.remove(int(a[1]))
    elif a[0] == "discard":
        s1.discard(int(a[1]))  

print(sum(s1)) 
