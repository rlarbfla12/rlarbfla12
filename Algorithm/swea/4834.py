T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int, input()))

    arr = [0] * 10
    for i in range(len(num)):
        arr[num[i]] += 1

    max_num = 0
    max_idx = 0
    for j in range(10):
        if max_num <= arr[j]:
            max_num = arr[j]
            max_idx = j

    print(f'{t+1} {max_idx} {max_num}')
