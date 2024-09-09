T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = ''

    # 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                result = arr[i][j:j+M]

    # 세로 탐색
    for j in range(N):
        for i in range(N-M+1):
            word = ''
            for k in range(M):
                word += arr[i+k][j]
            if word == word[::-1]:
                result += word

    print(f'#{t+1} {result}')




