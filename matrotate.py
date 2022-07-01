def solution(rows, columns, queries):
    mat = [[0]*columns for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = i*columns + j + 1
    answer = []        
    for x0,y0,x1,y1 in queries:
        temp = []
        temp += mat[x0-1][y0-1:y1]
        for r in range(x0,x1-1):
            temp.append(mat[r][y1-1])
        temp += mat[x1-1][y0-1:y1][::-1]
        for r in range(x1-2,x0-1,-1):
            temp.append(mat[r][y0-1])
        answer.append(min(temp))
        temp2 = [temp[-1]]+temp[:-1]
        
        k = 0
        for c in range(y0-1,y1):
            mat[x0-1][c] = temp2[k]
            k+=1
        for r in range(x0,x1-1):
            mat[r][y1-1] = temp2[k]
            k+=1
        for c in range(y1-1,y0-2,-1):
            mat[x1-1][c] = temp2[k]
            k += 1
        for r in range(x1-2,x0-1,-1):
            mat[r][y0-1] = temp2[k]
            k += 1            
    
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/77485