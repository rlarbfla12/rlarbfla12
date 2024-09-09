def func(n):
    if n <= N:                  # 존재하는 노드라면
        if tree[n] == 0:        # 그리고 값이 없으면
            tree[n] = func(n*2) + func(n*2+1)       # 자식노드 왼쪽 오른쪽 더해서
        return tree[n]          # 리턴 / 값 있으면 바로 리턴
    else:                       # 노드 없으면
        return 0                # 0 리턴

T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for m in range(M):
        v, i = map(int, input().split())
        tree[v] = i

    result = func(L)
    print(f'#{t+1} {result}')