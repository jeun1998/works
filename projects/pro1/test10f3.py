# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

def showGugu(start, end=5):
    for dan in range(start, end + 1, 1):
        print(str(dan) + '단 출력')
        for i in range(1, 10):
            print(f'{dan} * {i} = {dan * i}', end = ' ')
        print()

showGugu(2, 3)
print()
showGugu(2)
print()
showGugu(start=7, end=9)
print()
showGugu(end=9, start=7)
print()
showGugu(7, end=9)
# showGugu(start=7, 9) >>>> syntax error
# showGugu(end=9, 7) >>>> syntax error

print('가변 매개변수 ---')
def func1(*ar):   # * : 여러 개의 인자를 tuple로 묶어서 받겠다는 의미
    print(ar)

func1('김밥')   # ('김밥',)
func1('김밥', '비빔밥', '공기밥', '주먹밥') # ('김밥', '비빔밥', '공기밥', '주먹밥')

print()
def func3(w, h, **other):
    print(f'몸무게:{w}, 키:{h}')
    print(f'기타 : {other}')

func3(80, 174, irum='신기해', nai=33)
# func3(80, 180, {'irum':'신기해', 'nai':33}) >>> 에러

print()
def func4(a, b, *c, **d):
    print(a, b)
    print(c)
    print(d)

func4(1, 2)
func4(1, 2, 3, 4, 5)
func4(1, 2, 3, 4, 5, kbs=9, mbc=11)

print()
# type hint : 함수의 인자와 반환 값에 type을 적어 가독성 향상
# type에 대한 강제성은 없다.
def typeFunc(num, data):
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start=1):
        print(f'idx:{idx}, item:{item}')
        result[item] = idx

    return result

rdata = typeFunc('한개', ['일', '이', '삼'])
print(rdata)


