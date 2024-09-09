from itertools import combinations, product
# product : 데카르트 곱을 표현/모든 값에 대해 중첩을 허용하는 짝을 지어줌
# combinations :  조합 생성(원소의 개수 r개)


def solution(dice):
    n = len(dice)
    A = []  # 주사위 조합의 가능한 합을 저장할 리스트
    answer = []  # 최적의 주사위 인덱스를 저장할 리스트

    # 주사위 인덱스를 n//2개씩 뽑는 모든 조합 생성해 cases에 할당
    case = list(combinations(range(n), n // 2))
    for i in case:
        dices = []
        for j in i:
            dices.append(dice[j])

        # product를 사용하여 모든 조합 생성
        possible_combinations = product(*dices)

        # 각 조합의 합을 계산
        sums = []
        for k in possible_combinations:
            sums.append(sum(k))

        # 합 정렬
        num = sorted(sums)
        A.append(num)

    a = 0           # 최대 승리 횟수
    p = len(A)
    for pp in range(p):
        B = A[p - pp - 1]  # B와 A는 대칭구조를 가짐 (A리스트의 역순)

        # 각 조합이 이기는 횟수 이분탐색
        temp = 0
        for t in A[pp]:
            left, right = 0, len(B) - 1
            while left <= right:
                mid = (left + right) // 2
                if B[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            temp += left

        # 가장 승리 확률이 높은 경우의 수를 반환
        if a < temp:
            a = temp
            answer = []
            for x in case[pp]:
                answer.append(x + 1)

    return answer


# 입력값을 함수에 전달
dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
result = solution(dice)
print(result)