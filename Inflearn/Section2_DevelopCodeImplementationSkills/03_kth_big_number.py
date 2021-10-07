'''
### 문제 ###
## K번째 큰 수 ##
1. 1-100사이의 자연수가 적혀진 N장의 카드를 가지고있다. 같은 숫자의 카드가 여러장 있을수 있다
2. 카드를 3장씩 뽑아서 더한 수를 기록하려고 한다.
3. 3장씩 뽑아서 나올수 있는 모든 경우를 기록한다.
4. 기록한 값들중 K번째로 큰 수를 출력한다.
5. 중복된 수는 카운트 하지 않고 출력한다

### pseudo code ###
1. N 장의 카드를 순회하는 반복문 1을 만든다
2. 첫번째 반복문 안에서 첫번쨰 반복문의 기준하는 i 값보다 1큰수로 시작해서 N장의 카드를 순회하는 반복문 2를 만든다
3. 두번째 반복문 안에서 두번째 반복분의 시작점인 j 보다 1큰수로 시작하는 반복문을 만든다
4. set() 함수를 사용해서 자료형을 만든다 (중복하는 숫자를 제거하기 위해서)
5. 3중 반복문을 돌면서 set()함수로 만든 자료형에 담는다
6. 다 담아진 set()자료형을 list()자로형으로 바꾼다
7. 정렬한다
8. 뒤에서 3번째로 큰 수를 리턴한다
'''


def kth_big_number(N, K):
    _result = set()
    for i in range(len(N)):
        for j in range(i + 1, len(N)):
            for m in range(j + 1, len(N)):
                _result.add(N[i] + N[j] + N[m])

    result = list(_result)
    result.sort()
    print(result)
    return result[-K]


cards = [23, 6, 4, 5, 746, 785, 3]
K = 5
result = kth_big_number(cards, K)
print(result)
