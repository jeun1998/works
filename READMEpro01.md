# pro1 — Python 기본 문법과 객체지향 프로그래밍

> **학습 목표:** Python의 자료형·제어문·함수를 이해하고, 클래스로 객체 간 관계를 설계한다.

## 1. 핵심 이론

### ① 변수와 자료형
- `int`, `float`, `bool`, `str`은 기본적인 값의 종류이다. `type()`으로 자료형을 확인한다.
- `list`는 순서가 있고 변경할 수 있으며, `tuple`은 순서가 있지만 변경할 수 없다.
- `set`은 중복을 허용하지 않고, `dict`는 키와 값으로 정보를 관리한다.
- **가변 객체(list·dict 등)와 불변 객체(str·tuple 등)의 차이**를 알아야 함수 인수 전달과 복사 동작을 이해할 수 있다.

```python
scores = [80, 90, 85]
student = {'name': 'Kim', 'scores': scores}
print(student['name'], sum(scores) / len(scores))
```

### ② 조건문·반복문
- `if / elif / else`는 조건에 따라 실행 흐름을 분기한다.
- `for`는 반복 가능한 객체를 순회하고, `while`은 조건이 참인 동안 반복한다.
- `break`는 반복 종료, `continue`는 다음 반복으로 진행한다.
- 무한 반복을 피하려면 `while` 내부의 **종료 조건 변화**를 확인한다.

### ③ 함수와 스코프
- `def`로 함수를 선언하고 `return`으로 결과를 반환한다.
- 위치 인수, 키워드 인수, 기본 인수, `*args`, `**kwargs`의 차이를 이해한다.
- 지역 변수·전역 변수·`nonlocal`의 범위를 구분한다.
- **클로저(closure):** 외부 함수가 끝난 뒤에도 내부 함수가 바깥쪽 변수 상태를 기억하는 구조.
- **데코레이터(decorator):** 기존 함수를 수정하지 않고 호출 전후 동작을 확장한다.
- **재귀(recursion):** 함수가 자신을 다시 호출하며 반드시 종료 조건이 필요하다.

```python
def multiply_by(n):
    def inner(x):
        return x * n
    return inner

double = multiply_by(2)  # 클로저
print(double(5))          # 10
```

### ④ 객체지향(OOP)
- **클래스:** 속성과 동작을 묶은 설계도. **인스턴스:** 클래스로부터 생성한 객체.
- `__init__()`은 객체 생성 직후 초기화에 사용하고, `self`로 인스턴스 상태를 참조한다.
- **캡슐화:** 데이터와 동작을 묶고 사용 인터페이스를 명확하게 만든다.
- **상속:** 부모 클래스의 특성을 자식 클래스가 재사용한다 (`class Child(Parent)`).
- **오버라이딩:** 자식 클래스가 부모의 메소드를 다시 구현한다.
- **다형성:** 같은 메소드 호출이 객체의 구체적인 유형에 따라 다르게 작동한다.
- **추상 클래스:** `ABC`, `@abstractmethod`로 자식 클래스가 구현해야 할 공통 계약을 정의한다.
- **포함(composition):** 객체가 다른 객체를 부품으로 소유하는 구조 (`Car`가 `Handle`을 가짐).

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount): ...

class CashPayment(Payment):
    def pay(self, amount):
        return f'현금 {amount}원 결제'

print(CashPayment().pay(1000))
```

## 2. 실제 코드와 개념 연결

| 파일 | 핵심 학습 내용 |
|---|---|
| `test1.py` ~ `test4.py` | 기초 자료형, 연산자, 컬렉션, 정규표현식 |
| `test5if.py` ~ `test7for.py` | 분기·반복·중첩 반복 |
| `test8f1.py` ~ `test10f3.py` | 내장 함수, 사용자 함수, 다양한 인수 전달 |
| `test11closure.py`, `test12deco.py`, `test13recursive.py` | 클로저, 데코레이터, 재귀 |
| `test14module.py`, `test15module.py`, `pack1/` | 모듈·패키지 import |
| `test16graphic.py` ~ `test18opencv.py` | 그래픽·Pygame·OpenCV 입문 |
| `test19class.py` ~ `test26Lotto.py` | 클래스와 인스턴스, 포함 관계, 객체 활용 |
| `test27inherit.py` ~ `test34abstract_poly.py` | 상속·오버라이딩·다중상속·추상화·다형성 |
| `practice1.py`, `practice2.py`, `practice2a.py` | 반복문·급여 계산 등 기초 응용 |
| `practice3.py`, `practice3a.py` | 커피 자판기를 객체로 구현 |
| `practice4.py` ~ `practice6.py` | 전자제품/동물/급여 구조를 객체지향적으로 모델링 |

## 3. 실행 방법

```bash
cd projects/pro1
python test1.py
python test27inherit.py
python practice3a.py
```

표준 라이브러리 외의 예제(`pygame`, `cv2`)는 필요한 패키지와 이미지 파일을 준비해야 하며, GUI 환경이 필요할 수 있다. 일부 예제는 사용자 입력을 받는다.

## 4. 꼭 기억할 사항

1. `==`는 값 비교, `is`는 동일한 객체 여부를 확인한다.
2. 함수의 기본 인수에 `[]`처럼 변경 가능한 객체를 직접 사용하면 상태가 공유될 수 있다.
3. 클래스 변수와 인스턴스 변수의 범위가 다르다.
4. 다중 상속에서는 **MRO(Method Resolution Order)**가 메소드 탐색 순서를 정한다.
5. 클래스 설계에서는 상속이 적합한지, 다른 객체를 포함하는 편이 적합한지를 먼저 판단한다.

## 5. 스스로 점검하기

- `list`, `tuple`, `set`, `dict`의 차이를 예로 설명할 수 있는가?
- 클로저와 데코레이터의 실용적인 용도를 말할 수 있는가?
- 커피 자판기나 급여 계산 문제를 클래스·메소드로 분리할 수 있는가?
- 추상 클래스와 다형성을 이용해 새로운 결제/배송 방식을 추가할 수 있는가?

[⬅ 프로젝트 목록으로](../README.md)
