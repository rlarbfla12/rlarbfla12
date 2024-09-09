T = int(input())
for t in range(T):
    num, N = map(int, input().split())
    num_list = list(map(int, str(num)))
    change = num_list[:]

    cnt = 0
    max_v = 0
    min_v = 999999
    while cnt != N:
        for i in range(len(num_list)):
            if max_v < num_list[i]:
                max_v = num_list[i]
                max_idx = i

            if min_v > num_list[i]:
                min_v = num_list[i]
                min_idx = i

        change[min_idx] = max_v
        change[max_idx] = min_v
        cnt += 1

    print(f'#{t+1} {"".join(map(str, change))}')





