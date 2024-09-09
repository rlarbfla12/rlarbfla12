T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = []
    for i in range(N):
        oven.append(i)
    next = N  # 대기중인 피자 인덱스

    tmp = -1
    while oven:  # 남은 피자가 없을 때까지
        tmp = oven.pop(0)
        pizza[tmp] //= 2
        if pizza[tmp] > 0:  # 치즈가 남은경우 다시 투입(번호만)
            oven.append(tmp)
        elif pizza[tmp] == 0 and next < M:  # 치즈가 다 녹았고, 다음 피자가 있으면
            oven.append(next)  # 대기중인 피자 넣기
            next += 1
    print(f'#{t + 1} {tmp + 1}')