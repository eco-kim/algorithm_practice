def solution(a, b, g, s, w, t):
    answer = (10**9) * (10**5) * 4
    nn = len(g)
    low = 0
    high = (10**9) * (10**5) * 4

    while low <= high:
        mid = (low+high)//2
        gold, silver, total = 0,0,0

        for j in range(nn):
            g0, s0, w0, t0 = g[j], s[j], w[j], t[j]

            move_cc = mid // (t0*2)
            if mid % (t0*2) >= t0:
                move_cc += 1

            gold += min(g0, move_cc*w0)
            silver += min(s0, move_cc*w0)
            total += min(g0+s0, move_cc*w0)

        if gold>=a and silver>=b and total >= a+b:
            high = mid - 1
            answer = min(answer, mid)
        else:
            low = mid + 1

    return answer

#https://programmers.co.kr/learn/courses/30/lessons/86053