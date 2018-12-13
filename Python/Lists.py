# https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())
list1 = []
for i in range (n):
    a= input().strip().split(" ")
    if a[0] == "insert":
        z= int(a[2])
        list1.insert(int(a[1]),z)
    elif a[0] == "print":
        print(list1)
    elif a[0] == "remove":
        z1 = int(a[1])
        list1.remove(z1)
    elif a[0] == "append":
         z2= int(a[1])
         list1.append(z2)
    elif a[0] == "sort":
        list1.sort()
    elif a[0] == "pop":
        list1.pop()
    elif a[0] == "reverse":
        list1.reverse()
