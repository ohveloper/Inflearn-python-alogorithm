
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

