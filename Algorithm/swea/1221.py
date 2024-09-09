T = int(input())
for t in range(T):
    num_system = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    test_number, length = input().split()
    L = int(length)  # 길이 문자 -> 정수 타입으로 변환
    num_list = input().split()  # 입력 받은 문자들, 리스트화

    counts = [0] * 10  # 정수별 개수 확인 리스트 초기화
    for num in num_list:
        for i in range(10):
            if num == num_list[i]:
                counts[i] += 1  # 숫자 개수 추가

    result = []  # 새로 정렬할 빈 리스트 생성
    for j in range(10):
        for k in range(counts[j]):
            result.append(num_system[j])  # 개수만큼 문자 추가

    print(f'#{t+1}')
    print(*result)