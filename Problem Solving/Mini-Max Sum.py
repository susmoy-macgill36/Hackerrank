# https://www.hackerrank.com/challenges/mini-max-sum/problem
a = [int(i) for i in input().split()]

z1 = a[1] +a[2] + a[3] + a[4]
z2 = a[0] +a[2] + a[3] + a[4]
z3 = a[0] +a[1] + a[3] + a[4]
z4 = a[0] +a[1] + a[2] + a[4]
z5 = a[0] +a[1] + a[2] + a[3]
print(min(z1,z2,z3,z4,z5),max(z1,z2,z3,z4,z5))
