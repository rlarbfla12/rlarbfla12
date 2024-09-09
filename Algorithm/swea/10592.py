T = int(input())
for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    max_num = 0
    min_num = 100
    big = []
    small = []

    while num != []:
        for i in num:
            if max_num < i:
                max_num = i
        big.append(max_num)
        num.remove(max_num)

        for j in num:
            if min_num > j:
                min_num = j
        big.append(min_num)
        num.remove(min_num)

    print(big)
    print(num)