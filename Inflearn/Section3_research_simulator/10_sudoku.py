'''
# 스도쿠 문제 #
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.
'''

'''
## pseudo code ##
1. 행, 열, 3*3그룹. 이 세가지를 검사할수 있는 체크 리스트가 필요
    (ch_x, ch_y, ch_g) 0으로 채운 인덱스 9번까지의 리스트
[행, 열 검사 패턴]
2. 입력받은 2중 배열을 2중 반복문으로 순회한다
3. 2중 배열의 첫번째 배열을 순회한다
4. 해당 리스트의 0번째 인자의 값을 ch_x 리스트의 인덱스 번호로 하여 0을 1로 바꾼다
    예) 0번째 인자의 값이 3일 경우, ch_x 의 idx번호 3의 인자를 1로 바꾼다
5. 전부다 입력한 이후에 ch_x 리스트 내의 인자들의 합을 구해서 9가 아니면 false를 리턴한다
6. 9일 경우 ch_x의 값들을 0으로 초기화 시켜준후 다음 배열을 검사한다

[그룹 3*3 검사 패턴]
1. 2중 반복문을 돌때 x, y를 2중 배열의 1번째 부터 시작한다.
2. 늘려가는 수는 3씩 늘려간다, 1-4-7
3. arr[1][1] 자리를 기준할때 12시부터 시계방향으로 검사한다.
    arr[i-1][j+0], arr[i-1][j+1], arr[i+0][j+1],,,,arr[i-1][j-1]
4. ch_g 의 arr[i][j] idx 값을 1 로 바꾼다
5. 순회를 마친 이후에 다 더해서 9가 되면 통과 시키고 ch_g 배열을 초기화
6. 9가 아니면 false로 리턴 종료
'''


def ch_x(arr):
    l = len(arr)
    ch_x = [0] * (l + 1)

    for i in range(l):
        for j in range(l):
            ch_x[arr[i][j]] = 1

        if sum(ch_x) != l:
            return False
        else:
            ch_x = [0] * (l + 1)

    return True


def ch_y(arr):
    l = len(arr)
    ch_y = [0] * (l + 1)

    for i in range(l):
        for j in range(l):
            ch_y[arr[j][i]] = 1

        if sum(ch_y) != l:
            return False
        else:
            ch_y = [0] * (l + 1)

    return True


def ch_g(arr):
    l = len(arr)
    ch_g = [0] * (l + 1)
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(1, l, 3):
        for j in range(1, l, 3):
            test = [arr[i + dx[k]][j + dy[k]] for k in range(l)]
            for z in range(l):
                ch_g[test[z]] = 1

            if sum(ch_g) != l:
                return False
            else:
                ch_g = [0] * (l + 1)
    return True


def sudoku_check(arr):
    x = ch_x(arr)
    y = ch_x(arr)
    g = ch_g(arr)
    if x and y and g:
        return True, "YES"
    return False, "NO"


arr_true = [[1, 4, 3, 6, 2, 8, 5, 7, 9], [5, 7, 2, 1, 3, 9, 4, 6, 8], [9, 8, 6, 7, 5, 4, 2, 3, 1],
            [3, 9, 1, 5, 4, 2, 7, 8, 6], [4, 6, 8, 9, 1, 7, 3, 5, 2], [7, 2, 5, 8, 6, 3, 9, 1, 4],
            [2, 3, 7, 4, 8, 1, 6, 9, 5], [6, 1, 9, 2, 7, 5, 8, 4, 3], [8, 5, 4, 3, 9, 6, 1, 2, 7]]

print(ch_x(arr_true))
print(ch_y(arr_true))
print(ch_g(arr_true))

print(sudoku_check(arr_true))
