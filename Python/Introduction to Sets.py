# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array1):
    # your code goes here
    #set duplicate value remove kore dey
    return (sum(set(array1))/len(set(array1)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
