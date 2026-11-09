# pro2 — 예외 처리와 파일 입출력

> **학습 목표:** 파일을 안정적으로 읽고 저장하며 오류 상황을 처리하는 기본기를 익힌다.

## 1. 핵심 이론

### ① 예외(Exception) 처리
- `try`: 오류가 발생할 수 있는 코드.
- `except`: 지정한 예외에 대한 대응.
- `else`: 예외 없이 `try`가 끝난 경우 실행.
- `finally`: 정상/오류 여부와 무관하게 마무리 작업 수행.
- 가능한 한 `except Exception`보다 **구체적인 예외 타입**(`ValueError`, `FileNotFoundError`, `ZeroDivisionError`)을 사용한다.
- `raise`로 필요할 때 예외를 직접 발생시킬 수 있다.

```python
try:
    age = int(input('나이: '))
except ValueError:
    print('숫자를 입력하세요.')
else:
    print(f'{age}세')
finally:
    print('입력 처리 종료')
```

### ② 파일 입출력(I/O)
- `open(path, mode, encoding='utf-8')`으로 파일을 열고 `.read()`, `.readline()`, 파일 순회로 데이터를 읽는다.
- `r`은 읽기, `w`는 덮어쓰기, `a`는 이어쓰기, `b`는 바이너리 모드이다.
- `with open(...) as f:`는 블록을 빠져나갈 때 파일을 자동으로 닫아 **리소스 누수**를 방지한다.
- 문자열 데이터는 `strip()`으로 줄바꿈을 제거하고 `split()`으로 열을 분리할 수 있다.
- 파일의 인코딩이 다르면 `UnicodeDecodeError` 또는 한글 깨짐이 발생할 수 있다.

```python
sales = {}
with open('practice7data.txt', encoding='utf-8') as f:
    for line in f:
        values = line.strip().split()  # 실제 구분자는 원본 파일 형식에 맞게 조정
        if not values:
            continue
        # 읽은 행을 검증한 다음 딕셔너리에 누적
```

### ③ 경로와 직렬화
- 상대경로는 **현재 작업 폴더**를 기준으로 해석된다. 코드를 다른 위치에서 실행하면 파일을 찾지 못할 수 있다.
- `pathlib.Path(__file__).resolve().parent`로 현재 스크립트 기준 경로를 만들 수 있다.
- `pickle`은 Python 객체 저장에 편하지만 **신뢰할 수 없는 pickle 파일은 절대 역직렬화하면 안 된다**.

## 2. 실제 코드와 개념 연결

| 파일 | 학습 포인트 |
|---|---|
| `ex1try.py` | `try/except/else/finally`와 나눗셈 예외 |
| `ex2file.py` | `open()`, 읽기, 파일 시스템 확인 |
| `ex3file.py` | `with`, 쓰기·읽기, 객체 저장 실습 |
| `ex4zipcode.py` | 우편번호 텍스트를 행 단위로 읽어 지역 검색 |
| `practice7.py` | 판매 자료 집계, 딕셔너리 누적, 출력 파일 저장 |
| `exam1.py` | Bicycle 클래스로 객체 속성 복습 |

## 3. 실행 방법

```bash
cd projects/pro2
python ex1try.py
python ex4zipcode.py
python practice7.py
```

`ex4zipcode.py`는 `zipcode.txt`, `practice7.py`는 `practice7data.txt`가 필요하다. 예제에 따라 출력 파일이 생성되거나 덮어써질 수 있다.

## 4. 실무에서 중요한 체크리스트

- 파일 존재 여부, 입력 형식, 빈 줄, 잘못된 숫자 등을 검증했는가?
- 조회와 출력 파일 경로를 분리했는가?
- `w` 모드의 **기존 파일 덮어쓰기** 가능성을 알고 있는가?
- `with`를 사용해 파일을 반드시 닫는가?
- 예외를 단순히 무시하지 않고 실패 이유를 안내하는가?

[⬅ 프로젝트 목록으로](../README.md)
