
arr = [345,34,53,43,4,4,66,5,4,1,2,3,4,2,34,23,523,45,5,6]
pivot = arr[0]
less = [i for i in arr[1:] if i <= pivot]

print(less)

test = list(map(lambda x:x<pivot, arr))
print(test)

# 최악의 경우를 산정한 퀵정렬
def quicksort_badcase(arr):
    if len(arr) < 2: # 배열안의 요소가 하나만 남았을 경우 그 요소를 리턴시켜서 합친다
        return arr

    else:
        pivot = arr[0] # 기준을 정함
        less = [i for i in arr[1:] if i < pivot] # 기준보다 작은애들을 배열에 담는다
        greater = [i for i in arr[1:] if i > pivot] # 기준보다 큰 애들을 배열에 담는다
        same = [i for i in arr[1:] if i == pivot]

    return quicksort_badcase(less) + same + quicksort_badcase(greater) # 나눈 배열을 합치는데, 재귀호출하여 합친다
print(quicksort_badcase(arr))

# 이진 탐색을 활용한 퀵정렬
def quicksort(arr):
    if len(arr) < 2: # 배열안의 요소가 하나만 남았을 경우 그 요소를 리턴시켜서 합친다
        return arr

    else:
        pivot = arr[len(arr)//2] # 기준을 정함
        less = [i for i in arr if i < pivot] # 기준보다 작은애들을 배열에 담는다
        greater = [i for i in arr if i > pivot] # 기준보다 큰 애들을 배열에 담는다
        same = [i for i in arr if i == pivot]

    return quicksort(less) + same + quicksort(greater) # 나눈 배열을 합치는데, 재귀호출하여 합친다

qsort = quicksort(arr)
print(qsort)
print(sorted(arr))

## 인터넷에서 찾은 퀵정렬 예제
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
print(quick_sort(arr))