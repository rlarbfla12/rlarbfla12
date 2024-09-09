T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(N-1):
        min_num = num_list[i]
        min_num_idx = i
        for j in range(i+1, N):
            if min_num > num_list[j] :
                min_num = num_list[j]
                min_num_idx = j
        num_list[min_num_idx], num_list[i] = num_list[i], num_list[min_num_idx]
    print(f'#{t+1}', *num_list)