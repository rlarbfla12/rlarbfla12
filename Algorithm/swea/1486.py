def func(total, cnt):
    global ans

    if total >= B:
        ans = min(ans, total)
        return

    if cnt == N:
        return

    func(total + arr[cnt], cnt + 1)
    func(total, cnt + 1)

T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = int(1e9)
    func(0, 0)
    print(f'#{t+1} {abs(ans-B)}')