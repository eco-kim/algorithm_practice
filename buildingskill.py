def solution(board, skill):
    types = {1:-1,2:1}
    nr = len(board)
    nc = len(board[0])
    
    skills = [[0]*(nc+1) for j in range(nr+1)]
    
    for s in skill:
        r1,c1,r2,c2 = s[1:5]
        skills[r1][c1] += s[-1]*types[s[0]]
        skills[r2+1][c1] += s[-1]*types[s[0]]*(-1)
        skills[r1][c2+1] += s[-1]*types[s[0]]*(-1)
        skills[r2+1][c2+1] += s[-1]*types[s[0]]
    
    for j in range(nr):
        for i in range(1,nc):            
            skills[j][i] += skills[j][i-1]
            
    answer = 0
    for i in range(nc):
        c0 = 0
        for j in range(nr):
            skills[j][i] += c0
            c0 = skills[j][i]
            if board[j][i] + skills[j][i] >=1:
                answer += 1    
    return answer

    #https://school.programmers.co.kr/learn/courses/30/lessons/92344