def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = [-1] + list(map(int, input().split()))
student = int(input())

for i in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(num, N+1, num):      # 배수만 찾기
            change(j)
    else:       # 여자면
        change(num)     # 자기부터 바꿈, 좌우가 같든 틀리든 자신은 바꿔야 하니까
        for k in range(N//2):   # 반씩 탐색하니까 범위 반으로 두고
            if num + k > N or num - k < 1:  # 범위를 넘어가면 그만
                break
            if switch[num+k] == switch[num-k]:   # 좌우가 같을 시
                change(num+k)   # 바꿔줌
                change(num-k)
            else:   # 좌우가 다르면
                break       # 멈춰

for a in range(1, N+1):     # 20씩 끊어서 프린트 해주기
    print(switch[a], end = ' ')
    if a % 20 == 0:
        print()
