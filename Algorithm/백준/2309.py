nlst = []
T = 9
for t in range(T):
    N = int(input())
    nlst.append(N)

nlst.sort()
sum_num = sum(nlst)

for i in range(len(nlst)):
    for j in range(i+1, len(nlst)):
        if sum_num - nlst[i] - nlst[j] == 100:
            for k in range(len(nlst)):
                if k == i or k == j:
                    pass
                else:
                    print(nlst[k])
            exit()



