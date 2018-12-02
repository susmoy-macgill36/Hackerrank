# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotate(arr, k):
    return arr[k:] + arr[:k]

n,l = input().split(' ')
n1 = int(n)
l1 = int (l)
a = [int(i) for i in input().split()]

ss = rotate(a,l1)
for i in ss:
    print(i,end=" ")
