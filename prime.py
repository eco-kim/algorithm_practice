import math
from itertools import permutations

def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    root = math.ceil(n**(1/2))
    cc = 0
    for i in range(2,root+1):
        if n%i == 0:
            cc += 1
            break
    if cc == 0:
        return True
    else:
        return False
    
    
def solution(numbers):
    nn = len(numbers)
    answer = 0
    numset = set()
    for n in numbers:
        numset.add(int(n))
    for j in range(2,nn+1):
        perm = permutations(numbers, j)
        for p in perm:
            n = ''.join(list(p))
            numset.add(int(n))
            
    for n in numset:
        if prime(n):
            answer += 1

    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/42839