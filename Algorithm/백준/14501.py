n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)          # 날짜 별로 얻을 수 있는 최대 이익 저장

for i in range(n):          # i = 상담 시작 날짜
    for j in range(i + arr[i][0], n+1):     # j =  상담 끝나는 날짜
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])

