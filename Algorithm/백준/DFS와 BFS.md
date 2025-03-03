```python
from collections import deque

n, m, v = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)


dfs_list = []
def dfs(v):
    visited1[v] = 1
    dfs_list.append(v)

    for i in range(1, n+1):
        if arr[v][i] == 1 and visited1[i] == 0:
            dfs(i)


bfs_list = []
def bfs(v):
    queue = deque([v])
    visited2[v] = 1

    while queue:
        v = queue.popleft()
        bfs_list.append(v)

        for i in range(1, n+1):
            if visited2[i] == 0 and arr[v][i] == 1:
                queue.append(i)
                visited2[i] = 1

dfs(v)
bfs(v)
print(*dfs_list)
print(*bfs_list)
```
