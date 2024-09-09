def func(E):
    global graph
    global visited
    global stack

    while stack:
        a = stack.pop()
        visited[a] = 1
        if a == E:
            return 1
        for i in graph[a]:
            if visited[i] == 0:
                stack.append(i)
    return 0


T = 10
for t in range(T):
    N, num = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * (100)
    stack = []

    for i in range(num):
        s, e = arr[i*2], arr[i*2+1]
        graph[s].append(e)
        stack.append(0)

    result = func(99)
    print(f'#{t+1} {result}')


