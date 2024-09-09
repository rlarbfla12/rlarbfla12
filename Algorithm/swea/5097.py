from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int,input(). split()))

    q = [0] * N
    rear = -1

    for i in range(M):
        num = arr[(i + 1) % N]
        rear = (rear + 1) % N
        q[rear] = num
    print(f'#{t+1} {q[rear]}')


    # for i in range(M):
    #     arr.append(arr.pop(0))

    # q = deque(arr)
    # for i in range(M):
    #     first = q.popleft()
    #     q.append(first)
    #
    # print(f'#{t+1} {q[0]}')
