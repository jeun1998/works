
# 순차 탐색으로 특정 값의 위치 확인
def searchFunc(aa, x):
    n = len(aa)
    for i in range(0, n):
        if x == aa[i]:
            return i
    return -1

values = [17, 92, 18, 33, 55, 7, 32, 44]
print(searchFunc(values, 18))
print(searchFunc(values, 11))
print(searchFunc(values, 44))

print('\n정렬 알고리즘 ----')

# 정렬1) 선택 정렬 (selection sort)
# 방법1 : 이해 위주
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i

    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))

# 방법2 : 일반적인 방법
def sel_sort2(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort2(d)
print(d)
