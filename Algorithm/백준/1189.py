def dfs(row, col):
    global result
    # 목표지점에 도착하고
    if row == 0 and col == C - 1:
        # 이동 거리가 K이면 result + 1
        if graph[row][col] == K:
            result += 1
            return
        # 이동 거리 일치하지 않으면 그냥 함수 종료
        else:
            return

    # 모든 방향 탐색
    for i in move:
        # 새로 이동할 위치 계산
        rrow = row + i[0]
        ccol = col + i[1]
        # 이동할 위치가 그래프 내에 있고
        if 0 <=rrow < R  and 0 <= ccol < C:
            # 아직 방문하지 않은 곳이라면
            if graph[rrow][ccol] == '.':
                # 현재 거리에서 +1 값 저장
                graph[rrow][ccol] = graph[row][col] + 1
                # 다음 위치에서 dfs 실행
                dfs(rrow, ccol)
                # 탐색 끝나고 다니 .으로 되돌림
                graph[rrow][ccol] = '.'


R, C, K = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

# 상하좌우 방향 이동
move = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# 출발 지점 1로 설정 (왼쪽 아래)
graph[R-1][0] = 1

# K 값인 경로의 수 저장
result = 0

# 출발 점 왼쪽 아래 모서리
dfs(R-1, 0)
print(result)
