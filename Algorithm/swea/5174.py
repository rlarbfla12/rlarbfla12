def func(a):
    global cnt
    if a:
        cnt += 1
        func(left[a])
        func(right[a])

T = int(input())
for t in range(T):
    E, N = map(int,input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)
    par = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    cnt = 0
    root = N
    func(N)
    print(f'#{t + 1} {cnt}')
