def func(i, len_A, N, K):  # 원소의 개수 N, 원소의 합 K
    global result

    if i == len_A:
        cnt = 0
        ss = 0
        for j in range(len_A):
            if bit[j] == 1:
                ss += A[j]
                cnt += 1
        if ss == K and cnt == N:
            result += 1

    else:
        for j in range(1, -1, -1):
            bit[i] = j
            func(i + 1, len_A, N, K)

    return


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    len_A = 12
    bit = [0] * 12
    result = 0
    func(0, len_A, N, K)
    print(f'#{t + 1} {result}')

