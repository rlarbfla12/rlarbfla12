T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for i in range(N):
        if num[max_idx] <= num[i]:
            max_idx = i
        if num[min_idx] > num[i]:
            min_idx = i

    result = abs(max_idx - min_idx)
    print(f'#{t+1} {result}')
