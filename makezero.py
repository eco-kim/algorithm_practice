from collections import deque, defaultdict

def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    
    nn = len(a)
    tree = defaultdict(list)
    
    for b,c in edges:
        tree[b] += [c]
        tree[c] += [b]
    
    bfs = []
    setbfs = set()
    parent = [-1]*nn
    q = deque()
    q.append(0)
    while len(q)>0:
        node = q.popleft()
        bfs.append(node)
        setbfs.add(node)
        temp = tree[node]
        temp = set(temp) - setbfs
        for dau in temp:
            q.append(dau)            
            parent[dau] = node
    
    for idx in bfs[-1:0:-1]:
        n = a[idx]
        if n!= 0:
            answer += abs(n)
            a[parent[idx]] += n
    
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/76503