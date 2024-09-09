def func(N):
    global visited
    global stack
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while stack:
        i, j = stack.pop()
        if arr[i][j] == 3:
            return 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] != 1:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    stack = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sti, stj = i, j
                stack.append((sti, stj))
                visited[sti][stj] = 1

    result = func(N)
    print(f'#{t+1} {result}')