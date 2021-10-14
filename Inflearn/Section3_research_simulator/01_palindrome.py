'''
## 회문 확인 프로그램 ##
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''
'''
## pseudo code ##
1. N개의 문자열을 순회한다
2. i 번째 문자열을 전부 소문자로 바꾼다
3. i 번째 문자열을 뒤집어서 i 번째 문자열과 같은지 비교하여 출력
'''

def palindrome(arr):

    for i in arr:
        if i == i[::-1]:
            print(i, "YES")
        else:
            print(i, "NO")

palindrome(["hello", "world","you", "ollo"])

# a = 'ollo'
# print(a[::-1])
# print('ollo' == 'ollo')