
def add(a,b):
    c = a + b
    print(c)

add(3,2)

def add(a,b):
    c = a + b
    return c # return 을 만나면 함수는 종료된다

print(add(3,2))
x = add(3,2) # return 한 값을 변수에 할당
print(x)

# 여러 값을 튜플 형태로 리턴
def add(a,b):
    c = a+b
    d = a-b
    return c,d

x = add(3,2)
print(x)

# 스트링도 가능
def strstr(a,b,c):
    return a,b,c

x = strstr("hello",'world','!')
print(x)

# 함수를 분리하여 활용하는 방법
# 소수인지 아닌지 확인하는 함수
def isPrime(x):
    for i in range(2, x): # 나 자신 전까지 반복
        if x%i==0:
            return False # 나누어 떨어지는건 소수가 아니기 때문에 False
    return True # 2 부터 나 자신 전까지 다 돌고 나서 없으면 True

a = [12,13,8,2,49,231]
for y in a:
    if isPrime(y): # 소수인지 확인하는 함수를 호출해서 Ture, False 확인
        print(y, end=' ') # True이면 해당 수 프린트