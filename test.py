
# 변수명
# 1. 영문과 숫자로만 이루어 진다
# 2. 대소문자를 구분한다
# 3. 문자나, _ 로 시작한다
# 4. 특수 문자를 사용할수 없다
# 5. 키워드를 사용하면 안된다 (for, let, if 등등)

a = 1
A = 2
c = 5
print(a,A,c)

# 할당
a,b,c = 4,5,6
print(a,b,c)

a, b = 10, 20
print(a,b)

# 값 교환
a, b = b, a
print(a,b)

# 변수의 타힙
a = 1234 # int 정수형
print(type(a))
a = 12.123124234234234234234234 # float 실수형
print(type(a)) # 8바이트 까지만 출력 가능 64비트
a = 'student' # str 스트링
print(type(a))

# 출력 방식
print('number')
a,b,c = 1,2,3
print(a,b,c)
print('number: ', a,b,c)
print('number: ', a,b,c, sep=', ')
print('number: ', a,b,c, sep=',')
print('number: ', a,b,c, sep='\n')
print(a, end=' ')
print(b, end=' ')