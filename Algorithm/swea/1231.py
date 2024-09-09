def func(r):
    if r:
        func(left[r])
        print(words[r], end = '')
        func(right[r])

T = 10
for t in range(T):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    words = [''] * (N+1)

    for n in range(N):
        arr = input().split()
        num = int(arr[0])
        word = arr[1]
        left_idx = 0
        right_idx = 0

        if len(arr) > 2:
            left_idx = int(arr[2])
        if len(arr) == 4:
            right_idx = int(arr[3])

        words[num] = word
        if left[num] == 0 and left_idx != 0:
            left[num] = left_idx
        if right[num] == 0 and right_idx != 0:
            right[num] = right_idx
        if left_idx != 0:
            par[left_idx] = num
        if right_idx != 0:
            par[right_idx] = num

    c = N
    while par[c] != 0:
        c = par[c]
    root = c
    print(f'#{t+1}', end = ' ')
    func(root)
    print()

