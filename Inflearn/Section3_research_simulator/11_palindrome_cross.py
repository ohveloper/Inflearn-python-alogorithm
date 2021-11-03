'''
# 격자 펠린드롬 #
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지
구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
구부러진 숫자 목록은 카운트 하지 않는다
[자료구조와 알고리즘]
▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
'''
'''
# pseudo code #
- 가로검사 -
1. N행의 M번째부터 K번째 까지의 숫자를 검사한다
2. N은 일곱번째 행까지 검사한다 (0 -6)
3. M은 3번째까지만 검사한다 (0 -2)

-세로검사-
1. 
'''


def check(arr):
    cnt = 0
    for i in range(7):
        for j in range(3):

            ## 가로 검사를 위한 식
            ## i행을 다섯칸씩 3번 검사한다
            temp = arr[i][j:j + 5]
            revers_temp = list(reversed(temp))

            ## 앞서 reverse를 하지 않고 바로 뒤집은걸 검사할수 있음
            # if temp == temp[::-1]:
            if temp == revers_temp:
                # print(temp, revers_temp)
                # print("wow")
                cnt += 1

            ## 세로 검사를 위한 식
            ## 세로로 검사할때는 i를 고정시켜놓고 아래로 다섯칸씩 세번 검사
            ## 세로로 다섯칸 검사할때 출발점을 j로 놓고 검사하기 위해 arr[j+m] 부터 시작
            width = [arr[j + m][i] for m in range(5)]
            revers_width = list(reversed(width))
            if width == revers_width:
                # print(width,"!!",revers_width)
                # print("wow!!!")
                cnt += 1
    return cnt


test = check(
    [[1, 1, 2, 1, 1, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7],
     [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]])
print(test)
