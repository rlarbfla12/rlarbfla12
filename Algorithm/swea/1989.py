T = int(input())
for t in range(T):
    txt = input()
    N = len(txt)

    for i in range(N//2):
        if txt[i] == txt[N-1-i]:
            result = 1
        else:
            result = 0
    print(f'#{t+1} {result}')



