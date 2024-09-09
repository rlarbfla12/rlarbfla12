T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0]*i for i in range(1, N+1)]

    for n in range(N):
        arr[n][0] = 1
        arr[n][-1] = 1

    for i in range(1, N-1):
        for j in range(0, i):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]

    print(f'#{t+1}')
    for a in arr:
        print(*a)
