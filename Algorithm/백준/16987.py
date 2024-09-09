def dfs(n):
    global ans
    if n == N:      # 모든 계란에 대한 상태 확인
        total = 0
        for i in range(N):
            if arr[i][0] <= 0:      # 내구도 0 이하면
                total += 1          # 깨져있는 계란 개수

        ans = max(ans, total)
        return

    if arr[n][0] <= 0:
        dfs(n + 1)
        return

    check = True
    for i in range(N):
        if i == n:
            continue
        if arr[i][0] > 0:
            check = False
            break

    if check == True:           # 다 깨져있는 경우
        ans = max(ans, N-1)   # 자기 빼고 전부 다니깐 N-1
        return

    for i in range(N):
        if i == n or arr[i][0] <= 0:
            continue
        arr[n][0] -= arr[i][1]
        arr[i][0] -= arr[n][1]
        dfs(n + 1)
        arr[n][0] += arr[i][1]
        arr[i][0] += arr[n][1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  # 내구도, 무게
ans = 0
dfs(0)

print(ans)

