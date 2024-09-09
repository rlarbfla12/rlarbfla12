T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    max_num = 0
    min_num = 1000000
    for i in range(N-M+1):
        add_num = 0
        for j in range(i, i+M):
            add_num += num[j]
        if max_num < add_num:
            max_num = add_num
        if min_num > add_num:
            min_num = add_num

    result = max_num - min_num
    print(f'#{t+1} {result}')
