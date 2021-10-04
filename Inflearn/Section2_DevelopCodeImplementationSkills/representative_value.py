'''
## 문제 ##
N명의 학생의 수학점수가 주어집니다.
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

## pseudo code ##
1. 점수를 다 더해서 N으로 나누고 반올림한다
삭제 xx2. 빈 [] 를 만든다xx
2. minimum 변수를 만들어서 비교한다
3. 학생들의 점수를 순회한다
삭제 xx 4. 평균값에서 학생의 점수를 뺀 '절대값'을 빈 list에 순서대로 담는다 xx
4. 평균값 빼기 현재학생의 점수 를 절대값으로 감싸서 minimum 변수와 비교하고 더 작으면 minimum 변수를 교체한다
5. 전부 순회한 이후에 idx 값을 출력한다
'''
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
