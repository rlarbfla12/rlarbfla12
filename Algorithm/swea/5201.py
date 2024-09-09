T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    total = 0
    while len(truck) != 0 and len(container) != 0:
        mt = max(truck)
        mc = max(container)
        if mt >= mc:
            total += mc
            container.remove(mc)
            truck.remove(mt)
        else:
            container.remove(mc)

    print(f'#{t+1} {total}')


