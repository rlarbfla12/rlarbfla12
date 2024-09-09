def func(N):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = [start]


    while q:
        a, b = q.pop(0)
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0<=ni<N and 0<=nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[a][b] + 1
                if arr[ni][nj] == '0':
                    q.append((ni, nj))
                if arr[ni][nj] == '3':
                    return visited[ni][nj] - 2
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = (i, j)
                visited[i][j] = 1

    result = func(N)
    print(f'#{t+1} {result}')