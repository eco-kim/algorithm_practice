def solution(n, computers):
    def dfs(computer):
        nonlocal computers
        if sum(computers[computer]) == 0:
            return False
        else:
            for i, c in enumerate(computers[computer]):
                if c == 1:
                    computers[computer][i] = 0
                    dfs(i)
            return True  
    answer = 0
    for i in range(n):
        if dfs(i):
            answer += 1
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/43162