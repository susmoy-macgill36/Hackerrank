# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
a1 = input().split(' ')
b1= input().split(' ')
a = []
b =[]
for i in a1:
    a.append(int(i))

for i1 in b1:
    b.append(int(i1))
    
print(*product(a,b))   
# * = splat operator

exit()  
