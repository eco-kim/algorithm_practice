def solution(tickets):
    route = {}
    for t in tickets:
        route[t[0]] = route.get(t[0],[]) + [t[1]]
    for city in route:
        route[city].sort(reverse=True)
    stack = ['ICN']
    path = []
    while len(stack)>0:
        top = stack[-1]
        if top not in route or len(route[top])==0:
            path.append(stack.pop())
        else:
            stack.append(route[top][-1])
            route[top] = route[top][:-1]

    return path[::-1]

##https://programmers.co.kr/learn/courses/30/lessons/43164