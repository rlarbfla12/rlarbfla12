def func(n):
    global num
    if n <= N:
        func(n*2)
        tree[n] = num
        num += 1
        func(n*2+1)
    return tree[1], tree[N//2]

T = int(input())
for t in range(T):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    result = list(func(num))
    print(f'#{t+1} {result[0]} {result[1]}')

