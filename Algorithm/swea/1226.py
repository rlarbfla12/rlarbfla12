def func(i, j, N):
    global visited
    global stack
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack.append((i, j))
    visited[i][j] = 1

    while stack:
        a, b = stack.pop(0)
        if arr[a][b] == '3':
            return 1
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    return 0


T = 10
for t in range(T):
    n = int(input())
    arr = [list(input()) for _ in range(16)]
    stack = []
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                sti, stj = i, j

    result = func(sti, stj, 16)
    print(f'#{t+1} {result}')