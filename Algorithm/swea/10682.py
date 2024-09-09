def func(G):
    global graph
    global visited
    global stack
    while stack:
        node = stack.pop()
        if node == G:
            return 1
        if visited[node] == 0:
            visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                stack.append(i)
    return 0


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    stack = []
    for e in range(E):
        ss, gg = map(int, input().split())
        graph[ss].append(gg)
    S, G = map(int, input().split())
    stack.append(S)

    result = func(G)
    print(f'#{t+1} {result}')
