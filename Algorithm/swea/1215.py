T = 10
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            word = arr[i][j:j+N]
            if word == word[::-1]:
                cnt += 1

    for j in range(8):
        for i in range(8-N+1):
            word = ''
            for k in range(N):
                word += arr[i+k][j]
            if word == word[::-1]:
                cnt += 1

    print(f'#{t+1} {cnt}')

