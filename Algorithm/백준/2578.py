def func(arr):
    bingo_cnt = 0

    # 가로 빙고
    for row in range(5):
        if sum(arr[row]) == 0:
            bingo_cnt += 1

    # 세로 빙고
    for i in range(5):
        cntt = 0
        for j in range(5):
            if arr[i][j] == 0:
                cntt += 1
            if cntt == 5:
                bingo_cnt += 1

    # 대각선 빙고
    right = []
    left = []
    for i in range(5):
        right.append(arr[i][i])
        left.append(arr[i][4-i])

    if all(x == 0 for x in right) == 1:
        bingo_cnt += 1
    if all(y == 0 for y in left) == 1:
        bingo_cnt += 1

    if sum(right) == 0:
        bingo_cnt += 1
    if sum(left) == 0:
        bingo_cnt += 1

    return bingo_cnt

arr = [list(map(int, input().split())) for _ in range(5)]
say = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for i in range(5):      # say 돌기
    for j in range(5):
        for p in range(5):      # arr 빙고판 돌기
            for q in range(5):
                if say[i][j] == arr[p][q]:
                    arr[p][q] = 0
                    cnt += 1
                if cnt >= 12:
                    if func(arr) >= 3:
                        print(cnt)
                        exit()





