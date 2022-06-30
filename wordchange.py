from collections import deque

def solution(begin, target, words):
    inf = 9999
    dstdict = {}
    visit = []
    queue = deque([])
    for w in words:
        check = 0
        for i,s in enumerate(w):
            if s != target[i]:
                check += 1
        if check == 1 or check == 0:
            dstdict[w] = check
            queue.append(w)
        else:
            dstdict[w] = inf
            
    while len(queue)>0:
        target = queue.popleft()
        visit.append(target)
        d0 = dstdict[target]
        for w in words:
            if w not in visit:
                check = 0
                for i,s in enumerate(w):
                    if s != target[i]:
                        check += 1
                if check == 1:
                    dstdict[w] = min(d0+1,dstdict[w])
                    queue.append(w)
                    visit.append(w)
    answer = inf
    for w in dstdict:
        check = 0
        for i, s in enumerate(w):
            if s != begin[i]:
                check += 1
        if check == 1:
            answer = min(dstdict[w]+1, answer)
            
    if answer == inf:
        answer = 0
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/43163
###리팩토링 필요.
