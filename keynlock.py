def turn(key):
    m = len(key)
    newkey = [[0]*m for j in range(m)]
    for i in range(m):
        for j in range(m):
            newkey[j][m-i-1] = key[i][j]
    return newkey

def solution(key, lock):
    m, n = len(key), len(lock)
    nn = 2*m+n-2
    for i in range(4):
        for j in range(m+n-1):
            for k in range(m+n-1):
                temp = [[0]*(nn) for l in range(nn)]
                for a in range(m):
                    for b in range(m):
                        temp[j+a][k+b] = key[a][b]
                cc = 0
                for a in range(n):
                    for b in range(n):
                        if temp[m-1+a][m-1+b]+lock[a][b]!=1:
                            cc = 1
                            break
                    if cc == 1:
                        break
                if cc == 0:
                    return True
        key = turn(key)
    return False

#https://programmers.co.kr/learn/courses/30/lessons/60059
