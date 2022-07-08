def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: int((x*4)[:4]), reverse=True)    
    answer = ''.join(numbers)

    return str(int(answer))

#https://school.programmers.co.kr/learn/courses/30/lessons/42746﻿
