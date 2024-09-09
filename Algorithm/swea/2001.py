T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0       # 잡은 파리 최댓값
    for i in range(N-M+1):
        for j in range(N-M+1):
            num = 0         # 잡은 파리의 수
            for a in range(i, i+M):
                for b in range(j, j+M):
                    num += arr[a][b]

            if total < num:
                total = num
    print(f'#{t+1} {total}')