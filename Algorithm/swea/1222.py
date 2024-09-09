T = 10
for t in range(T):
    N = int(input())
    num = list(input())
    stack = []
    result = ''

    for i in num:
        if i == '+':
            while stack:
                result += stack.pop()
            stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()

    total = []
    for j in result:
        if j == '+':
            total.append(total.pop() + total.pop())
        else:
            total.append(int(j))
    print(f'#{t+1} {total[-1]}')
