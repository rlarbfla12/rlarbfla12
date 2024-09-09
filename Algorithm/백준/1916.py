import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)

heap = []

for _ in range(m):
    node1, node2, value = map(int, input().split())
    graph[node1].append((node2, value))

start, end = map(int, input().split())

heapq.heappush(heap, [0, start])
dist[start] = 0

while heap:
    cost, node = heapq.heappop(heap)  # 순서 수정
    if cost > dist[node]:
        continue

    for nextnode, nextcost in graph[node]:
        distance = nextcost + cost

        if dist[nextnode] > distance:
            dist[nextnode] = distance
            heapq.heappush(heap, [distance, nextnode])

print(dist[end])
