'''
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.
두번쨰 입력 정보가 1 이면 오른쪽으로 0이면 왼쪽으로

'''
N = int(input("N : "))
arr = [list(map(int, input("arr : ").split())) for _ in range(N)]
where = int(input("where? : "))
lr = int(input("left==0, right==1 : "))
M = int(input("how many move? : "))

def dried_persimmon(N,arr,where,lr,M):
    if lr == 0:
        arr[where - 1] = mix_list_left(N, M, arr[where - 1])
        return arr
    else:
        arr[where - 1] = mix_list_left(N, M, arr[where - 1])
        return arr

def mix_list_left(N, M, a):
    b = list(a)
    for _ in range(M):
        for i in range(N):
            if i == N - 1:
                b[i] = a[0]
            else:
                b[i] = a[i + 1]
        a = list(b)
    return a


def mix_list_right(N, M, a):
    b = list(a)
    for _ in range(M):
        for i in range(N):
            if i == 0:
                b[i] = a[N - 1]
            else:
                b[i] = a[i - 1]
        a = list(b)
    return a


test = dried_persimmon(N,arr,where,lr,M)
print(test)

def last_dance(arr):
    s = 0
    N = len(arr)
    e = N
    res = 0
    num = 1
    for i in range(N):
        for j in range(s, e):
            res += arr[i][j]

        s += num
        e -= num
        print(s,e)
        if s == N // 2:
            print("hello")
            num *= -1



    return res

result = last_dance(test)
print(result)