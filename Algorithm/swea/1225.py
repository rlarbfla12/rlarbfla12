T = 10
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    while arr[7] != 0:
        for i in range(1, 6):
            num = arr.pop(0)
            num -= i
            if num <= 0:
                num = 0
            arr.append(num)
            if arr[7] == 0:
                break
    print(f'#{t+1}', *arr)
