# https://www.hackerrank.com/challenges/capitalize/problem
z= input()
k= z.split(" ")
m = []
for i in k:
   
   m.append(i.capitalize())
print (' '.join([str(item) for item in m]))

exit()
