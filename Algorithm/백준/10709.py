H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
brr = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            brr[i][j] = 0
            nj = j + 1
            while 0 <= nj < W:
                brr[i][nj] = nj - j
                nj += 1

for row in brr:
    print(*row)


