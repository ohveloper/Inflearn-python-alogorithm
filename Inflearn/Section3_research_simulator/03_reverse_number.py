'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓 여있다. 각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다: 구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면, 위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다. 이제 전체 카드가 놓인 순서는 아래 그림과 같다.
이 상태에서 구간 [9, 13]이 다시 주어진다면, 위치 9부터 위치 13까지의 카드 6, 5, 11, 12, 13을 역순으로 하여 13, 12, 11, 5, 6으로 놓는다. 이제 전체 카드가 놓인 순서는 아래 그림 과 같다.
오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치 를 구하는 프로그램을 작성하시오.
'''


# start:s, end:e
def reverse_cards(s, e):

    # 0부터 20까지의 인덱스를 가지는 리스트 생성
    card_list = list(range(21))

    # e자리와 s자리를 바꾸고, e -1 과 s + 1 자리를 바꾸면 되기 때문에 절반만 검사
    for i in range((e - s + 1) // 2):

        card_list[s + i], card_list[e - i] = card_list[e - i], card_list[s + i]

    else:

        # 0번째 0은 제거하기 위해 pop(0)
        card_list.pop(0)
        return card_list


print(reverse_cards(3, 5))
