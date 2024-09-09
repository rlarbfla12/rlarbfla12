def solution(users, emoticons):
    answer = [0, 0]             # 플러스 가입자 수, 총 수익
    data = [10, 20, 30, 40]     # 할인율
    discount = []               # 모든 할인율 조합을 저장할 리스트

    def dfs(tmp, d):            # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):       # 모든 할인율을 할당했다면
            discount.append(tmp[:])     # 현재 조합을 discount에 추가, tmp복사본
            return
        else:                   # 그렇지 않으면
            for i in data:
                tmp[d] += i     # 각 할인율에 +i
                dfs(tmp, d+1)   # 다음 인덱스로 이동 후, 재귀호출
                tmp[d] -= i     # 원래 상태로 돌리기 위해 -i

    dfs([0] * len(emoticons), 0)        # 모든 할인율 조합 생성

    for disc in discount:           # 만들어진 모든 조합 확인
        cnt = 0                     # 플러스 유저 가입 수
        get = 0                     # 조합으로 얻은 총 수익
        for i in users:
            pay = 0                 # 각 유저가 지불한 금액
            for j in range(len(disc)):          # 각 이모티콘에 대해
                if i[0] <= disc[j]:             # 유저가 원하는 할인율이 현재 할인율보다 작으면
                    pay += emoticons[j] * (100 - disc[j]) / 100     # 할인된 가격으로 이모티콘 구매 후, 가격 저장
                if pay >= i[1]:     # 지불 금액이 유저 예산 초과하면
                    break           # 구매 중지
            if pay >= i[1]:
                pay = 0             # 유저의 지불금액 0
                cnt += 1            # 플러스 가입자 수 +1
            get += pay              # 총수익에 유저 지불 금액 더함

        if cnt >= answer[0]:        # 현재 최대값을 넘어가면 갱신
            if cnt == answer[0]:    # 플러스 가입자 수가 최대값과 같다면, 수익을 갱신
                answer[1] = max(answer[1], get)
            else:                   # 그렇지 않으면, 최대 가입자 수와 수익을 모두 갱신
                answer[1] = get
            answer[0] = cnt         # 플러스 가입자 수 갱신

    return answer
