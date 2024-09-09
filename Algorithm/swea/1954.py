T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for t in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    cnt = 1
    direction = 0
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N:

        ni = i + di[direction]
        nj = j + dj[direction]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            direction = (direction + 1) % 4

    print(f'#{t+1}')
    for a in arr:
        print(*a)
