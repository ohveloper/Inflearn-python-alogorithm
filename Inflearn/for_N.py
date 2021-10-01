
# n = int(input(n))
n = 10
for i in range(1,n+1, 2):
    print(i)

for j in range(1,n+1):
    if j % 2 == 1:
        print(j)

### 9. 리스트와 내장함수(2)

a = [1,2,3,4,5]
for x in enumerate(a): # index를 찾아줌
    print(x)
    print(x[1])

# enumerate(), index와 value를 ( , ) 튜플 형태로 반환
for index, value in enumerate(a):
    print(index, value)

# all(), 한번이라도 거짓이면 거짓
if all(3 > x for x in a): # 문법 정확하게 맞춰서 써야됨
    print('yes')
else:
    print('no')

# any(), 한번이라도 참이면 참
if any(0 > x for x in a): # 문법 정확하게 맞춰서 써야됨
    print('yes')
else:
    print('no')


### 10. 2차원 배열 접근
