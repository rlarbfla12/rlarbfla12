white = [[0] * 100 for _ in range(100)]

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    white[a][b] = 1
    for i in range(10):
        for j in range(10):
            white[a+i][b+j] += 1

cnt = 0
for p in range(100):
    for q in range(100):
        if white[p][q] != 0:
            cnt += 1

print(cnt)


