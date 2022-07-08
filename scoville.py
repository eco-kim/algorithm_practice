import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while len(scoville)>1:
        a = heapq.heappop(scoville)
        if a>=K:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
    
    if scoville[0]<K:
        answer = -1
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/42626
