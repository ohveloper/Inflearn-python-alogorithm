'''
# 사과농장 (다이아몬드) #
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
'''

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


# z = [3,2,5,6,2,1]
# b = [[0] * i for i in z]
#
# # print(a)
# print(b)
'''
최초 풀이
def apple_tree_diamond(n, arr):
    s = e = n // 2
    res = 0
    num = 1

    for i in range(n):
        for j in range(s, e + 1):
            res += arr[i][j]

        s -= num
        e += num
        if s == 0:
            num *= -1

    return res


print(apple_tree_diamond(n, a))

'''


def apple_tree_diamond2(n, arr):

    # 더하기를 시작할 중간지점을 s,e 에 담는다
    s = e = n // 2
    res = 0

    # 첫번째 반복문, 행을 담당
    for i in range(n):

        # 두번째 반복문, 행 안에서 더할 범위를 s, e로 지정
        for j in range(s, e + 1):

            # 현재 행과 현재 위치를 더하기 j가 1씩 증가 i 는 고정
            res += arr[i][j]

        # s,e에 맞춰서 행을 탐색하고 나면 현재 위치한 행이 중간인지 아닌지를 분기하여 변화
        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return res


print(apple_tree_diamond2(n, a))
