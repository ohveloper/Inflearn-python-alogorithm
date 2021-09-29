


# break가 걸리면 else 출력 x
for i in range(1,11):
    print(i)
    if i == 5:
        break
else:
    print(11)

# 정상적으로 반복문을 다 돌면 else 출력
for i in range(1,11):
    print(i)
    if i == 20:
        break
else:
    print(11)