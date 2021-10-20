'''
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
[자료구조와 알고리즘]
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

N = 5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
출력값
155
'''
'''
## pseudo code ##
1. 함수 4개를 만든다
    1. 가로로 다 더하는 함수
    2. 세로를 다 더하는 함수
    3. 대각선을 다 더하는 함수
    4. 역 대각선을 다 더하는 함수
2. 리스트에 합들을 다 담는다
3. 그 중 가장 큰 수를 리턴 한다
'''
N = int(input())

# 2차원 배열을 입력받는 방법
# 1 2 3 /  4 5 6 / 7 8 9
arr = [list(map(int, input().split())) for _ in range(N)]
print(N, arr)


def sum_width(arr):
    return sum(arr)


def grating_numbers(arr):
    result = []
    N = len(arr)
    temp_slash = 0
    temp_reverse = 0
    temp_height_sum = 0

    # 가로 더하는 반복문
    for i in arr:
        result.append(sum_width(i))

    # 역 슬래시 더하는 반복문 0,1,2,3... 순서로 == 역슬래시
    for idx, item in enumerate(arr):
        temp_reverse += item[idx]
        print(idx, item)
    result.append(temp_reverse)

    # 슬래시 더하는 반복문 N, N-1, N-2,,,, 역순으로 == 슬래시
    for idx, item in enumerate(arr):
        temp_slash += item[N - idx - 1]
    result.append(temp_slash)

    # 세로로 더해가는 반복문
    for i in range(N):
        for j in range(N):
            temp_height_sum += arr[j][i]
        result.append(temp_height_sum)
        temp_height_sum = 0

    return max(result), result


print(grating_numbers(arr))
