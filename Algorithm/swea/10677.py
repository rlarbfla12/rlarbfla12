T = int(input())
for t in range(T):
    N = int(input())
    n = N // 10

    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 3
    for i in range(3, n+1):
        arr[i] = arr[i-1] + 2 * arr[i-2]
    print(f'#{t+1} {arr[n]}')

