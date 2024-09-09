T = 10
for t in range(T):
    N, num = map(str, input().split())
    stack = []

    for i in num:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    result = ''.join(stack)
    print(f'#{t+1} {result}')