'''
## K번째 약수 ##
# N과 K를 입력받아 N의 약수들 중에 K번째로 작은 수를 출력한다
## pseudo code ##
1. N을 순회한다. len(N)까지. count = 0 을 생성
2. 나머지가 0인수는 약수이므로 count += 1 을 한다
3. count == K 가 될때 순회중인 i를 출력한다
4. 끝까지 돌아도 count가 K에 도달하지 못하면 -1를 리턴한다
'''
n, k = map(int, input().split()) # n과 k를 입력받는 함수


def find_kth_factor(N, K):
    count = 0 # 몇번째 인지 기억할 변수
    for i in range(1, N + 1): # 약수는 1부터 카운트 가능하기때문에 1과 나 자신까지
        if N % i == 0: # 나머지가 0이면 약수
            count += 1
        if count == K: # count가 K번째에 도달하면 return
            return i
    else:
        return -1 # 아무것도 찾지 못하면 -1 return


answer = find_kth_factor(n, k) # return 해줬기 때문에 변수에 할당
print(n, k)
print(answer) # 할당된 값을 프린트
