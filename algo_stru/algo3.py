# 삽입(insertion) 정렬 : 앞에서부터 하나씩 꺼내, 자기자리 찾아 끼워넣는 정렬
# 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 부분집합과 비교하여, 자신의 위치를 파악

# 방법1 : 이해용 - 추가 공간이 있음
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print('a(d) : ', a)
        print('result : ', result)

d = [2,4,5,1,3]
print(find_ins_idx(d, 4))

# 방법2 : 일반적 - 추가 공간이 거의 없음