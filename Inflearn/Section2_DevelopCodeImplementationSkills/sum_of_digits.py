'''
N개의 자릿수가 입력되면 각 자리수의 합을 구하고 가장 큰수를 리턴
이때 digit_sum(x) 함수를 꼭 활용한다
예) 12, 2345, 999 // 27

## pseudo code ##
입력받은 숫자가 담겨있는 배열을 순회한다
각자리수를 더하는 digit_sum(x) 함수를 활용하여 다 더한수를 max 와 비교한다
max를 리턴한다
'''

# 입력받은 숫자의 각 자릿수의 합을 구하는 함수
def digit_sum(x):
    result = 0

    # 계속 나눠서 1의자리수를 10으로 나눈 몫은 0이되기때문에 멈춤
    while x > 0:

        # 입력받은 수를 10으로 나눈 나머지가 1번째 자리
        result += x % 10

        # 입력받은 수를 10으로 나눈 몫은 1의자리를 제외한 10의자리부터 숫자
        x = x // 10

    return result

# 입력받은 어레이의 가장 큰 수를 찾는 함수
def max_digit(arr):
    result = 0
    for i in arr:

        # 각자리수의 함을 구하는 함수를 사용해서 최대값을 비교
        _max = digit_sum(i)
        if _max > result:
            result = _max
    return result


print(digit_sum(123))
print(max_digit([123,534,23,45,32,444444444,999]))