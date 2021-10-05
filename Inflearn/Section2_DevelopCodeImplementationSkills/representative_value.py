'''
## 문제 ##
N명의 학생의 수학점수가 주어집니다.
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''

'''
## 어려웠던 헷갈렸던 포인트
분기를 나누는 포인트가 햇갈렸던거 같다. 경우의 수를 나누는 연습을 더 해야겠다.
1. 갭차이가 적은걸 정답으로 삼는다
2. 갭차이가 같으면 스코어가 더 큰걸로 바꾼다
    여기서 큰걸로 바꾼다가 분기를 나눠주는 포인트
    갭차이가 같을때 현재 숫자가 이전 숫자보다 커야지만 바뀔수 있다.

## 변수명의 중요성, 변수명을 제대로 작성 안하니까 내가 더 헷갈린다.
목적을 분명히 하고 정확하게 필요한 변수명을 작성해야 변수명만 보고도 흐름이 파악 되겠다
'''
def result(N, arr):
    ave = int(sum(arr)/N + 0.5)
    minimum_gap = 2147000000
    result = 0
    index = 0

# 입력받은 수학점수가 담긴 arr를 순회한다 (idx, score) 로 나눠서 받는다
    for idx, score in enumerate(arr):

        # 평균과 점수의 갭을 절대값으로 담아둔다
        gap = abs(score - ave)

        # 가장 작은 갭보다, 현재의 갭이 작으면 조건문을 수행한다
        if gap < minimum_gap:
            result = score
            minimum_gap = gap
            index = idx + 1

        # 가장 작은 갭과, 현재의 갭이 같을경우 분기를 한번더 나눠서 처리한다
        elif gap == minimum_gap:

            # 갭이 같을경우 스코어가 큰 수를 담아야 하기때문에 분기를 작동시킨다
            if result < score:
                result = score
                index = idx + 1

    # 반복문을 전부다 수행한 뒤에 점수와, 해당 학생의 번호를 출력한다
    return result, index, ave

print(result(5, [12,334,534,5623,4523]))
'''
## 첫번째 잘못 이해한 풀이
from functools import reduce


def find(N, arr):
    average = round(reduce(lambda x, y: x + y, arr)/N)
    a_values = []
    minimum = 100
    idx = 0
    for i in range(len(arr)):
        # a_values.append(abs(average-i))
        _min = abs(average - arr[i])
        if _min < minimum:
            minimum = _min
            idx = i

    return idx


result = find(10, [1, 2, 3, 4, 5, 23])
print(result)

print(round(3.5))
'''

