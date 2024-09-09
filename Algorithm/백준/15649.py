N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
path = [0] * M

def func(a, start):
    if a == M:
        print(*path)
        return

    for k in range(start, N):
        path[a] = arr[k]
        func(a+1, k+1)

func(0, 0)