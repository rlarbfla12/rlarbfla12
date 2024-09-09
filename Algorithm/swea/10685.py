T = int(input())
for t in range(T):
    words = input()
    stack = []

    for i in words:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{t+1} {len(stack)}')
