'''
# 문제, N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서 s번째부터 e번째까지의 수를
오름 차순 정렬 했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요
# 첫번째 입력받는 정보들 : n(숫자가 몇개인지), s(시작점), e(끝점), k(몇번째)
# 두번째 입력받는 정보들 : 숫자들을 연속해서 입력받는다 (받아서 배열로 변경)

## pseudo code ##
1. n,s,e,k를 각각 입력받는다
2. n개의 숫자열을 입력받는다 ( 입력 받는 숫자는 받아서 리스트화 한다)
3. 입력받은 숫자열을 s부터 e까지 슬라이스 한다 (이때 시작하는 숫자와 인덱스가 다르기 때문에 -1해주기)
4. 슬라이스한 숫자열에서 k번째 수를 찾아서 리턴한다 (k번째 숫자와 실제 인덱스가 다르기 때문에 -1해주기)
'''


def find():
    n, s, e, k = map(int, input().split())
    unsorted_list = list(map(int, input().split()))

    # K번째 수를 찾는 함수를 분리
    def find_nth_number(n, s, e, k, a):
        slice_list = a[s - 1:e]
        sorted_list = sorted(slice_list)
        return sorted_list[k - 1]

    result = find_nth_number(n, s, e, k, unsorted_list)
    return result


# result = find_nth_number(n,s,e,k,unsorted_list)
# print(result)
result = find()
print(result)
