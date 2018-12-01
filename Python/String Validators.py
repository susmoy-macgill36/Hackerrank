# https://www.hackerrank.com/challenges/string-validators/problem
a = input ()

print(any(i.isalnum() for i in a))
print(any(i.isalpha() for i in a))
print(any(i.isdigit() for i in a ))
print(any(i.islower() for i in a))
print(any(i.isupper() for i in a))
