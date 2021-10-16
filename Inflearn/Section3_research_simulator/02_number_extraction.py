'''
## 문제: 숫자만 추출 ##
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉첫자리0은자연수화할때무시합니다. 출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
'''
'''
pseudo code
1. 숫자만 필터하는 함수를 만든다
2. 숫자만 필터해서 int로 만든다
3. 약수의 개수를 리턴한
'''

def is_number(x):
    res = ''
    for i in x:
        if i.isdigit():
            res += i
    return int(res)

def cnt_measure(x):
    num = is_number(x)
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return num, cnt

print(cnt_measure("hel0lo1wo0r0ld"))

# print(is_number("hello0002233world"))
# z = 'hello'
# m = 'world'
# print(z + m)