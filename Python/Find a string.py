# https://www.hackerrank.com/challenges/find-a-string/problem

def findAstring(string, subString):
    startpoint = 0
    match = 0

    while True:
        startpoint = string.find (subString, startpoint)

        if startpoint < 0:
            break

        startpoint += 1
        match += 1

    return match


mainString = input()
subString = input()
print (findAstring(mainString,subString))
