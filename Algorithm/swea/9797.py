def bfs(s, g, v):  # 출발 s, 도착 g, 노드 개수 v
    q = []  # 큐 생성
    visited = [0] * (v + 1)  # visited 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 인큐 1로 표시

    while q:  # 큐가 빌 때까지 반복
        t = q.pop(0)  # 처리할 정점 디큐
        if t == g:  # 도착 노드와 같아지면
            return visited[t] - 1  # 최단 경로 간선 수
        for j in adjl[t]:  # t의 인접 정점 하나씩 꺼내기
            if visited[j] == 0:  # 인큐 되지 않았으면
                q.append(j)  # 인큐
                visited[j] = visited[t] + 1

    return 0  # G까지 경로가 없는 경우


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    # 인접 리스트
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):  # for i in range(0, E*2, 2)
        n1, n2 = map(int, input().split())  # n1, n2 = arr[i], arr[i+1]
        adjl[n1].append(n2)
        adjl[n2].append(n1)  # 무향그래프
    S, G = map(int, input().split())  # 출발 노드, 도착 노드

    result = bfs(S, G, V)

    print(f'#{t + 1} {result}')
