N, K = map(int, input().split())
arr = [[0] * 6 for _ in range(2)]
total = 0
for t in range(N):
    S, Y = map(int, input().split())
    arr[S][Y-1] += 1

for each in arr:
    for i in each:
        if i % 2 == 0:
            total += i // 2
        else:
            total += i // 2 + 1

print(total)


