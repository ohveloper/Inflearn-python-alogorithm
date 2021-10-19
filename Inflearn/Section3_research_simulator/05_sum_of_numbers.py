'''
## 수들의 합 ##
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가
M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
'''
## pseudo code ##
1. lt, rt = 0, 1 포인터를 만든다
2. rt가 N보다 커질때까지 반복한다
3. tot 변수를 만든다 초기값은 수열의 0번째 값
4. 분기를 만든다
5. tot가 M보다 작을경우 rt를 더하고 오른쪽으로 한칸 민다
6. tot가 M과 같을경우 cnt += 1 을 해주고 tot에서 lt값을 빼고 lt를 옆으로 한칸 옮긴다
7. tot가 M보다 클 경우 tot에서 lt 값을 빼고 옆으로 한칸 옮긴다 
8. rt 가 N보다 커지면 종료
'''


def sum_of_numbers(N, M, arr):
    lt = 0
    rt = 1
    cnt = 0
    tot = arr[0]

    while True:
        if tot < M:

            # 중요 # arr[rt]값을 tot에 더한 이후에 옆으로 밀어야 하는데 더할 값이 없기 때문에
            # 중요 # else로 분기를 설정해서 while 문을 종료시킨다
            if rt < N:
                tot += arr[rt]
                rt += 1
            else:
                break
        elif tot == M:
            cnt += 1
            tot -= arr[lt]
            lt += 1
        elif tot > M:
            tot -= arr[lt]
            lt += 1
        else:
            break
    return cnt


print(sum_of_numbers(8, 3, [1, 2, 1, 3, 1, 1, 1, 3]))
