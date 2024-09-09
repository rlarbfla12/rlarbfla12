def msort(m):
    if len(m) == 1:  # 원소가 하나만 남은 경우
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = msort(left)  # 왼쪽 절반 분할
    right = msort(right)  # 오른쪽 절반 분할
    return merge(left, right)  # 다시 합친 결과 리턴


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(left) + len(right))
    i = j = 0  # i : 왼쪽 배열에서 비교할 위치, j : 오른쪽 배열에서 비교할 위치
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[i + j] = left[i]
            i += 1
        else:
            result[i + j] = right[j]
            j += 1
    while i < len(left):  # left의 원소만 남은 경우
        result[i + j] = left[i]
        i += 1
    while j < len(right):
        result[i + j] = right[j]
        j += 1
    return result


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = msort(arr)
    print(f'#{t + 1} {arr[N // 2]} {cnt}')