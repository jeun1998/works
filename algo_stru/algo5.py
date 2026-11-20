# 정렬은 분할 정복 기반의 고성는 정렬 알고리즘

# 기본 동작 방식
# 1. 피벗 선택 : 배열 안에서 하나의 원소를 고른다
# 2. 분할 : 피벗을 기준으로 작은 값을 왼쪽으로, 큰 값은 오른쪽으로 재배치
# 3. 재귀 : 피벗으로 인해 나눠진 왼쪽 부분 배열과 오른쪽 부분 배열에 대해 동일
# 4. 종료 : 부분 배열의 크기가 0이나 1이 되면 정렬이 완료

# 하나의 기준점을 중심으로 작은값과 큰 값을 나눠서 각각 정렬후 마지막에 이어 붙이는 방법

# 방법 1 : 이해 위주
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a

    pivot = a[-1]

    g1 = []
    g2 = []

    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    print(f'g1{id(g1)} : {g1}')
    print(f'g2{id(g2)} : {g2}')
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6,8,3,1,2,4,7,5]
print(quick_sort(d))

print('----------------')

# 방법 2 : 일반 알고리즘
def quick_sort2_sub(a, start, end):
    if end - start <= 0:
        return

    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            print(f'{a[i]}, {a[j]} = {a[j]}, {a[i]}')
            i += 1

    a[i], a[end] = a[end], a[i]
    print(f'{a[i]}, {a[end]} = {a[end]}, {a[i]}')

    quick_sort2_sub(a, start, i - 1)
    quick_sort2_sub(a, i + 1, end)

def quick_sort2(a):
    quick_sort2_sub(a, 0, len(a) - 1)

d = [6,8,3,1,2,4,7,5]
quick_sort2(d)
print(d)