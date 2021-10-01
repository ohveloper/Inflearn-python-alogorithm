
def plus_one(x):
    return x+1

x = plus_one(1)
print(x)

# lambda 표현식으로 작성
plus_two = lambda x:x+2
print(plus_two(1))

# list와 map을 활용
a=[1,2,3]
print(list(map(plus_one,a)))

# list와 map에 lambda 활용
a=[1,2,3]
print(list(map(lambda x:x+2, a)))

print(list(map(int, ["1","2"])))