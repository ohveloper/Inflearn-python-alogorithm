
a = [0] * 3
print(a)

# 2차원 list 만들기
b = [[0] * 3 for _ in range(3)]
print(b)

# 2차원 리스트 값에 접근
b[0][1] = 1
print(b)

b[1][2] = 2
print(b)

# 2차원 리스트를 표처럼 보이게 출력
for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=' ')
    print()