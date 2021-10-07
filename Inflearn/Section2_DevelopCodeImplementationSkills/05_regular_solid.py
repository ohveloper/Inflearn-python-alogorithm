'''
## 정다면체 ##
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.

## pseudo code ##
1. 빈 배열을 만든다
2. N을 순회한다
3. N 안에서 M을 순회한다
4. 작성한 배열에 N 과 M을 더한 수를 idx로 하여 value 를 +1 해준다
5. 가장 많이 나온 수를 max_count_number에 넣는다
6. 넣는법은 카운트한 배열을 순회하면서 max_count_number 보다 큰 수를 만나면 clear한 이후에 바꿔준다
7. 만약 max_count_number와 같으면 append한다
'''


def find_max_chance_number(N, M):
    temp_list = [0] * (N + M + 3) #! +3 수정
    max_count_number = 0
    result_list = []

    # 1 부터 N까지 순회하는동안, 1부터 N까지 순회한다
    for i in range(1, N + 1): #! +1 수정
        for j in range(1, M + 1 ): #! +1 수정

            # 1 + 1, 1 + 2, 1 + 3,,,,2 + 1,,,,4 + 6 까지 순회하면서 추가
            n = i + j
            temp_list[n] = temp_list[n] + 1

    # idx는 더해서 나온 수, k는 벨류, 즉 k는 몇번 나왔는지 카운트된 벨류
    for idx, k in enumerate(temp_list):

        # 만약 k가 현재까지 나온 k들보다 크면 작동하는 분기
        if k > max_count_number:
            max_count_number = k
            result_list.clear()
            result_list.append(idx)

        # 만약 k가 현재까지 나온 들과 같다면 작동하는 분가
        elif k == max_count_number:
            result_list.append(idx)

    return result_list, temp_list


print(find_max_chance_number(4, 6))
