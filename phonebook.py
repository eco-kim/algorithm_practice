from collections import defaultdict

def solution(phone_book):
    answer = True
    headdict = defaultdict(int)
    for p in phone_book:
        nn = len(p)
        for j in range(nn):
            headdict[p[:j+1]] += 1
    
    for p in phone_book:
        if headdict[p]>1:
            answer = False
            break
    
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/42577