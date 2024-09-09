T = int(input())
for t in range(T):
    w = input()
    arr = input()

    max_cnt = 0
    for i in w:
        cnt = 0
        for j in arr:
            if i == j:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{t+1} {max_cnt}')

