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


def apple_tree_diamond2(n, arr):
    s = e = n // 2
    res = 0

    for i in range(n):
        for j in range(s, e + 1):
            res += arr[i][j]
        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return res


print(apple_tree_diamond2(n, a))
