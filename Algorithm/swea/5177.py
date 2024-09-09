def func(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = c // 2

    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2


def sum_num(n):
    total = 0
    while n > 1:
        n = n // 2
        total += h[n]
    return total

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    h = [0] * (N+1)
    last = 0
    for i in arr:
        func(i)
    result = sum_num(N)
    print(f'#{t+1} {result}')
