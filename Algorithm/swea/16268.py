T = int(input())
dj = [0, 1, 0, -1]
di = [1, 0, -1, 0]
direction = 0
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for i in range(N):
        for j in range(M):
            result = arr[i][j]

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:
                    result += arr[ni][nj]

            if max_num < result:
                max_num = result

    print(f'#{t+1} {max_num}')




