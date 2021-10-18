'''
## 두 리스트 합치기 ##
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
## sort() 사용 금지
'''
'''
# pseudo code #
1. p1, p2 포인터가 필요
2. p1 포인터는 a 리스트를 0번째 인덱스부터 가르킴
3. p2 포인터는 b 리스트를 0번째 인덱스부터 가르킴
4. p1 과 p2를 비교해서 작은수를 c 리스트에 append
5. p1, p2포인터중 먼저 끝에 도달하면 break
6. 나머지 리스트의 남은 부분을 잘라서 c에 붙이기
'''
# 풀이 1, 입력받은 a,b 리스트에서 맨 앞단의 수를 비교해가면서 빼내는 방법
def merge_list1(a,b):
    result = []

    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a[0])
            a.pop(0)
        else:
            result.append(b[0])
            b.pop(0)

    result += a + b

    return result

print(merge_list1([1,1,2,3],[1,2,3,4]))

# 풀이 2, 입력받은 a,b는 그대로 두고 포인터를 이동시켜서 풀이
def merge_list2(a,b):
    result = []
    p1 = 0
    p2 = 0
    N = len(a)
    M = len(b)

    while p1 < N and p2 < M:
        if a[p1] <= b[p2]:
            result.append(a[p1])
            p1 += 1
        else:
            result.append(b[p2])
            p2 += 1

    if p1 < N:
        result += a[p1:]
    else:
        result += b[p2:]

    return result

print(merge_list2([1,2,3,4,5,6],[1,3,4,5,6,8]))
