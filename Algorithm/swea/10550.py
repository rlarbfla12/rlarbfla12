T = int(input())
for t in range(T):
    num = int(input())

    arr = [0] * 12
    for j in range(6):
        arr[num % 10] += 1
        num //= 10

    j = 0
    tri = 0
    ran = 0
    while j < 10:
        if arr[j] >= 3:
            arr[j] -= 3
            tri += 1
            # continue

        if arr[j] >= 1 and arr[j+1] >= 1 and arr[j+2] >= 1:
            arr[j] -= 1
            arr[j+1] -= 1
            arr[j+2] -= 1
            ran += 1
            # continue
        j += 1

    if tri + ran == 2:
        print(f'#{t+1} {"Baby Gin"}')
    else:
        print(f'#{t+1} {"Lose"}')



