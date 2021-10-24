'''
첫번째 풀이와 거의 유사하지만 코드 작성 순서화
조건문을 분기하는 방식이 달랐다! all() 메소드를 사용하여 풀이
'''

n = int(input())
arr = [list(map(int, input("arr : ").split())) for _ in range(n)]

arr.insert(0, [0] * n)
arr.append([0] * n)

for x in arr:
    x.insert(0, 0)
    x.append(0)

print(arr)

# 출력값과 시계방향을 나타내는 dx, dy 12, 3, 6, 9 순서대로 표현
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n+1):

        # all()메소드를 활용해서 12시 방향부터 시계방향으로 반복하면서 확인후 전부 true 면 작동
        if all(arr[i][j] > arr[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
