'''
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.
두번쨰 입력 정보가 1 이면 오른쪽으로 0이면 왼쪽으로

'''
# a = [1,2,3]
# N = len(a)
M = 2
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

a = arr[2]

def mix_list_left(M, a):
    b = list(a)
    for _ in range(M):
        for i in range(N):
            if i == N - 1:
                b[i] = a[0]
            else:
                b[i] = a[i+1]
        a = list(b)
    return a

# a[0], a[1], a[2] = a[2],a[0],a[1]
print(a)

def mix_list_right(M, a):
    b = list(a)
    for _ in range(M):
        for i in range(N):
            if i == 0:
                b[i] = a[N-1]
            else:
                b[i] = a[i - 1]
        a = list(b)
    return a

print(mix_list_right(M,a))
# z = [123,124,234]
# z = mix_list_left(M,a)
# print(z)

