T = int(input())
for t in range(T):
    arr = list(input().split())
    stack = []  # 빈 스택 만들기
    error = False

    for i in range(len(arr) - 1):  # 마지막 . 제외하고 돌아주기 위해 -1
        if arr[i].isdigit():  # arr[i]가 숫자라면
            stack.append(int(arr[i]))  # stack에 추가
        elif arr[i] in '*/+-':  # arr[i]가 연산자이고
            if len(stack) < 2:  # stack의 길이가 2보다 작으면
                error = True  # error
                break
            a = stack.pop()  # 아니면 a를 pop
            b = stack.pop()  # b도 pop
            if arr[i] == '+':  # +, - , *, / 연산해주기
                result = b + a
            elif arr[i] == '-':
                result = b - a
            elif arr[i] == '/':
                result = b // a
            elif arr[i] == '*':
                result = b * a
            stack.append(result)  # 결과 다시 stack에 추가
        else:  # 숫자도 연산자도 아니면 error
            error = True

    if error == True or len(stack) != 1:  # error고, stack의 길이가 1이 아니면
        print(f'#{t + 1} error')  # error
    else:  # 에러도 아니고, 길이도 1이면
        print(f'#{t + 1} {stack.pop()}')  # 그거 pop




