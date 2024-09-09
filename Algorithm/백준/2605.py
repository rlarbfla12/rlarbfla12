# N = int(input())
# arr = list(map(int, input().split()))
# real = []
# num = []
# for i in range(1, 6):
#     num.append(i)
#     for j in range(i-1, i):
#         if arr[j] == 0:
#             real.append(i)
#         else:
#             real.insert(i-arr[j]-1, i)
#
# print(*real)

N = int(input())
arr = list(map(int, input().split()))
real = []

for i in range(N):
    if arr[i] == 0:
        real.append(i + 1)
    else:
        real.insert(i - arr[i], i + 1)

print(*real)


