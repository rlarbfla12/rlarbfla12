arr = [[0] * 100 for _ in range(100)]

for n in range(4):
    b, a, d, c = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] += 1

cnt = 0
for p in range(100):
    for q in range(100):
        if arr[p][q] != 0:
            cnt += 1

print(cnt)

