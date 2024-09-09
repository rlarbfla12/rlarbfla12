T = 10
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    view = 0
    for i in range(2, N-2):
        if arr[i-2] > arr[i-1]:
            front_arr = arr[i-2]
        else:
            front_arr = arr[i-1]
        if arr[i+2] > arr[i+1]:
            back_arr = arr[i+2]
        else:
            back_arr = arr[i+1]
        if front_arr > back_arr:
            high_arr = front_arr
        else:
            high_arr = back_arr
        if arr[i] > high_arr:
            view += arr[i] - high_arr

    print(f'#{t+1} {view}')
