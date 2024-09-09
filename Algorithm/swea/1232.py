def func(n):
    if par[n]:          # par[n]이 존재한다면
        if par[n] == '+':
            return func(left[n]) + func(right[n])
        elif par[n] == '-':
            return func(left[n]) - func(right[n])
        elif par[n] == '*':
            return func(left[n]) * func(right[n])
        elif par[n] == '/':
            return func(left[n]) // func(right[n])
        else:           # 숫자인 경우
            return int(par[n])
    else:
        return 0


T = 10
for t in range(T):
    N = int(input())
    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for n in range(N):
        arr = list(input().split())
        par[int(arr[0])] = arr[1]
        if len(arr) > 2:
            left[int(arr[0])] = int(arr[2])
        if len(arr) == 4:
            right[int(arr[0])] = int(arr[3])

    result = func(1)
    print(f'#{t+1} {result}')