T = int(input())
for t in range(T):
    txt = input()
    stack = []
    result = 0

    for i in txt:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if stack != []:
                if (i == ')' and stack[-1] == '(') or (i =='}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    break
            else:
                break

    else:
        if stack == []:
            result = 1

    print(f'#{t+1} {result}')
