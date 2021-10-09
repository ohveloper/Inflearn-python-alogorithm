'''
## 뒤집은 소수 ###
N개의 자연수를 입력받고 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램
reverse(x)함수와 isPrime(x) 함수를 반드시 작성하여 풀이
910을 뒤집으면 19가 된다
'''


# 입력받은 수를 뒤집는 함수
def reverse(x):
    res = 0

    while x > 0:
        # 나머지는 1의자리
        t = x % 10

        # 현재 숫자의 마지막에 0을 붙여주고 1의자리를 더한다
        res = res * 10 + t

        # 10으로 나눈 몫은 1의자리를 지우면서 0을 지운다
        x = x // 10

    return res

# 소수인지 아닌지 판별
def isPrime(x):
    if x == 1:
        return False

    # 16의 절반까지만 검사해보면 됨 절반인 숫자가 있다는건 약수가 있다는것
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


def findPrime(arr):
    for i in arr:
        rev = reverse(i)
        if isPrime(rev):
            print(rev)


findPrime([12, 423, 1, 34, 3456, 23, 234, 235, 3, 32,2113, 7])
