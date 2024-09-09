T = 10
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    col_max = 0
    row_max = 0
    for i in range(100):
        col_sum = 0
        row_sum = 0
        for j in range(100):
            col_sum += arr[i][j]
            row_sum += arr[j][i]

        if col_max < col_sum:
            col_max = col_sum

        if row_max < row_sum:
            row_max = row_sum

    dia_1 = 0
    dia_2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                dia_1 += arr[i][j]
                dia_2 += arr[j][i]

    if col_max < row_max:
        result1 = row_max
    else:
        result1 = col_max
    if dia_1 < dia_2:
        result2 = dia_2
    else:
        result2 = dia_1
    if result1 < result2:
        total = result2
    else:
        total = result1

    print(f'#{t+1} {total}')



