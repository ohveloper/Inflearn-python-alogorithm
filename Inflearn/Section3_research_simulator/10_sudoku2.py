'''
# 수도쿠 문제 해설 들은 이후 다시 작성해보기 #

[포인트]
1. 가로 세로 검사를 한번에 하기
2. 그룹검사를 중간중간 False검사 할수 있게 짜보기
'''


def check_sudoku(arr):
    # 행과 열을 한번에 조사 할 수 있는 2중 반복문
    for i in range(9):

        # 행을 바꿀때마다 초기화를 해줘야 하기 때문에
        ch_x = [0] * 10
        ch_y = [0] * 10

        for j in range(9):
            # 행0 고정, 열을 0,1,2,3,.,,
            ch_x[arr[i][j]] = 1

            # 열0 고정, 행을 0,1,2,3,,,,
            ch_y[arr[j][i]] = 1

        if sum(ch_x) != 9 or sum(ch_y) != 9:
            return False

    ## 그룹을 검사할 반복문
    # 행의 시작지점을 지정하기 위해
    for i in range(3):

        #  열의 시작지점을 지정하기 위해
        for j in range(3):

            # 돌아올때마다 초기화
            ch_g = [0] * 10

            ## 실제 작동하는 부분
            # 0 행(k)의 0,1,2 열(m)을 검사
            # 1 행(k)의 3,4,5 열(m)을 검사
            for k in range(3):
                for m in range(3):
                    ch_g[arr[i * 3 + k][j * 3 + m]] = 1

            if sum(ch_g) != 9:
                return False

    return True


arr_true = [[1, 4, 3, 6, 2, 8, 5, 7, 9], [5, 7, 2, 1, 3, 9, 4, 6, 8], [9, 8, 6, 7, 5, 4, 2, 3, 1],
            [3, 9, 1, 5, 4, 2, 7, 8, 6], [4, 6, 8, 9, 1, 7, 3, 5, 2], [7, 2, 5, 8, 6, 3, 9, 1, 4],
            [2, 3, 7, 4, 8, 1, 6, 9, 5], [6, 1, 9, 2, 7, 5, 8, 4, 3], [8, 5, 4, 3, 9, 6, 1, 2, 7]]
arr_false = [[2, 4, 3, 6, 2, 8, 5, 7, 9], [5, 7, 2, 1, 3, 9, 4, 6, 8], [9, 8, 6, 7, 5, 4, 2, 3, 1],
             [3, 9, 1, 5, 4, 2, 7, 8, 6], [4, 6, 8, 9, 1, 7, 3, 5, 2], [7, 2, 5, 8, 6, 3, 9, 1, 4],
             [2, 3, 7, 4, 8, 1, 6, 9, 5], [6, 1, 9, 2, 7, 5, 8, 4, 3], [8, 5, 4, 3, 9, 6, 1, 2, 7]]

if check_sudoku(arr_true):
    print("YES")
else:
    print("NO")