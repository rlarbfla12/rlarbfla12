def mini(i, k):
    global min_num

    if i == k:
        num_sum = 0
        for j in range(k):
            num_sum += arr[j][P[j]]
        if min_num > num_sum:
            min_num = num_sum

    else:
        for j in range(i, k):
            P[i],P[j] = P[j], P[i]
            mini(i+1, k)
            P[i],P[j] = P[j], P[i]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_num = 100
    mini(0, N)

    print(f'#{t+1} {min_num}')