T = int(input())
for t in range(T):
    w = input()
    arr = input()

    if w in arr:
        result = 1
    else:
        result = 0

    print(f'#{t+1} {result}')
