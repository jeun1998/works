# LinearList(선형구조 - Array, List) 연습
# 놀이공원(공연장) 줄서기

# 연습1 - python 함수 사용
line = ['철수','영희','민수']
print('현재 줄 상태 : ', line)
print()

# 데이터 접근 - 인덱스를 사용(빠름)
print('맨 앞사람 : ', line[0])
print('두번째 사람 : ', line[1])
print()

# 새치기(삽입)
line.insert(2, '지수')  # 민수는 다음자리로 밀림
print('지수 삽입 후 현재 줄 상태 : ', line)
print()

# 줄에서 빠지기(삭제)
line.remove('영희')  # 1번째 이후 자료가 앞으로 한칸씩 이동
print('영희가 빠진후 줄 상태 : ', line)
print()

# 앞사람 부터 놀이기구 타기 - 첫번째 자료부터 빠져나감. 뒤자료는 앞으로 이동
first_person = line.pop(0)  # pop(0):왼쪽값 추출, pop() 오른쪽값 추출
print('첫번째 사람 입장 후 남은 줄상태:', line)
print()

# 현재 남은 사람 번호와 함께 출력
for i, p in enumerate(line):
    print(i, '번째 사람:', p)
print('**' * 10)

# 연습2 - python 코드를 사용
line = ['철수','영희','민수']
print('현재 줄 상태 : ', line)
print()

# 데이터 접근 - 인덱스를 사용(빠름)
print('맨 앞사람 : ', line[0])
print('두번째 사람 : ', line[1])
print()

# 중간에 새로운 사람이 삽입 : '철수','영희','민수'에서 지수를 민수 앞에 끼워넣기
# index 2 위치에 지수 삽입 - 공간확보 -> index 2 이후 뒤로 한 칸씩 이동 -> 값 대입
line.append(None)  # 공간 확보
for i in range(len(line) - 1, 2, -1):
    line[i] = line[i - 1]
print(line)
line[2] = '지수'
print('지수가 삽입된 후 줄 상태:', line)
print()

# 줄에서 대기하던 사람(영희) 줄서기 포기 - 삭제
# 영희의 위치를 찾고, 그 뒤 요소들을 앞으로 이동
remove_index = None
for i in range(len(line)):
    if line[i] == '영희':
        remove_index = i
        break

# 앞으로 한 칸씩 이동
for i in range(remove_index, len(line) - 1):
    line[i] = line[i + 1]
print(line)
line.pop()  # 마지막 중복 자료 제거
print('영희가 빠져 나간 후 줄 상태 :', line)

# 앞사람 한명이 놀이기구 타기 입장
# 앞에서 부터 한 칸 씩 좌측으로 이동
first_person = line[0]
for i in range(0, len(line) - 1):
    line[i] = line[i + 1]

print(line)
line.pop()
print('남아 있는 줄상태 : ', line)

# 현재 남은 사람 번호와 함께 출력
for i, p in enumerate(line):
    print(i, '번째 사람:', p)

# LinearList는 index로 즉시 접근 가능, 삽입/삭제 시 데이터 이동 발생(비용) - 비효율적


print('===================================================================')

# 연결된 리스트 (Linked List)
# 자료를 임의의 공간에 기억시키고, 순서에 따라 포인터로 자료를 연결시킨 구조

# 놀이공원에 줄서기
class Node:
    def __init__(self, name):
        # 이름과 다음 사람을 가리키는 next를 가짐
        self.name = name
        self.next = None   # pointer

# 연결 리스트를 관리
class LinkedList:
    def __init__(self):
        self.head = None  # 맨 앞사람 주소(list의 시작점)

    # 새로운 Node를 추가(줄 뒤에 다음 사람 추가)
    def append(self, name):
        new_node = Node(name)   # 새 Node 생성

        if self.head is None:  # 줄(List)이 비어 있는 경우
            self.head = new_node
            return
        
        # 줄의 맨 끝 사람 찾기(이미 노드가 있다면 마지막 노드까지 이동)
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def show(self):
        # print(line.head)
        # print(line.head.next)
        # print(line.head.next.next)
        current = self.head
        while current:
            print(current.name, end=" -> ")
            current = current.next
        print('끝')

    # 특정 사람 뒤에 새사람 끼워 넣기
    # traget 노드를 찾고 -> 새 노드 만들고 -> 기존 연결 변경
    def insert_after(self, target_name, new_name):
        current = self.head

        while current:
            if current.name == target_name:
                new_node = Node(new_name)  # 지수 객체 생성
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    # 특정 사람 삭제
    def remove(self, name):
        # 맨 앞사람이 나가는 경우
        if self.head and self.head.name == name:
            self.head = self.head.next  # head를 두번째 노드의 주소를 변경
            return
        
        # 첫 노드가 삭제 대상이 아닌 경우
        current = self.head
        while current and current.next:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

line = LinkedList()
line.append('철수')   # 추가
line.append('영희')
line.append('민수')

print('현재 줄 상태 : ')
line.show()
print()

# 영희 뒤에 지수를 삽입
line.insert_after('영희', '지수')
print('지수를 삽입 줄 상태 : ')
line.show()
print()

# 영희가 줄서기를 포기 (삭제)
line.remove('영희')
print('영희 삭제 후 줄 상태 : ')
line.show()
print()

print('=======================================================')


# Stack : LIFO 구조

stack = []   # 파있너의 List를 Stack 처럼 사용
print('놀이 공원 입장')
print()

# 놀이 기구 탈 때의 기록을 남김
stack.append('T-express 탑승')  # PUSH
print('기록 : ', stack)

stack.append('바이킹 탑승')
print('기록 : ', stack)
# print(stack[1])   # 주의 : 파이썬의 List 기능. Stack 아님

stack.append('회전목마 탑승')
print('기록 : ', stack)

# 가장 최근 기록 삭제
last_action = stack.pop()   # POP    주의 : pop(0), pop(1) 사용X 개념 위반
print('마지막 기록 취소 후 현재 : ', stack)

last_action = stack.pop()
print('마지막 기록 취소 후 현재 : ', stack)


print('\n--------------')
# LIFO를 class로 연습
class MyStack:
    def __init__(self, iterable = None):
        self._data = []  # 클래스 내부 저장소 임을 알림(가독성), 기본문법X
        if iterable is not None:
            for x in iterable:
                self.push(x)

    def push(self, x):
        # 맨 위 (top)에 요소 추가(삽입)
        self._data.append(x)
        return x
    
    def pop(self):
        # 맨 위 (top)에 요소 제거
        if not self._data:
            raise IndexError('스텍이 비어 있음')
        return self._data.pop()
    
    def is_empty(self):
        return not self._data   # 비었을 때 True 반환
    
    def __repr__(self):  # 파이썬 실행시(print) 자동호출되는 특별 메소드
        top_to_bottom = list(reversed(self._data))
        return f'Stack(top -> bottom {top_to_bottom})'

def demo1Func():
    s = MyStack()
    for item in ['A', 'B', 'C', 'D']:
        s.push(item)
        print(f'push {item} -> ', s)
    # print(s._data)
    print('LIFO에 따라 하나씩 추출')
    while not s.is_empty():
        print('pop -> ', s.pop(), "|현재는:", s)

def demo2Func(text : str) -> str:
    s = MyStack(text)
    out = []  # 뒤집힌 문자 기억
    while not s.is_empty():
        out.append(s.pop())
    return ''.join(out)

if __name__ == '__main__':
    demo1Func()
    print(demo2Func('Python is good'))
    print(demo2Func('파이썬 만세'))




print('==========================================================')


# Queue : FIFO 구조
from collections import deque  # list 대신 deque를 Queue 구현
# deque 주료 메소드
# deque(), append(1) :우측에 추가, appendleft(1) :좌측에 추가
# pop() : 우측 제거, popleft() : 좌측 제거  ...

# 놀이 공원 대기 줄
queue = deque()
print('놀이 공원 기구 대기 시작')

# 줄서기
queue.append('철수')
print('첫번째 줄서기 : ', list(queue))
queue.append('영희')
print('두번째 줄서기 : ', list(queue))
queue.append('민수')
print('세번째 줄서기 : ', list(queue))

print()
# 놀이 기구 탑승 - FIFO
first_person = queue.popleft()  # queue에서 제거
print(first_person, '놀이 기구 탑승')
print('현재 대기줄 : ', list(queue))
print()

# 한명 더 놀이 기구 탑승 - FIFO ( 중간 데이터 처리 불가 )
first_person = queue.popleft()  # queue에서 제거
print(first_person, '놀이 기구 탑승')
print('현재 대기줄 : ', list(queue))
print()

if queue:
    print('탑승 예정자:', queue[0])
else:
    print('대기자 없음')


print('\n---------------------------------')
# FIFO를 class로 연습
class Queue:
    def __init__(self, iterable = None):
        self._data = deque()
        if iterable is not None:
            for x in iterable:
                self.enqueue(x)
    
    def enqueue(self, x):
        self._data.append(x)  # back에 요소 추가
        return x
    
    def dequeue(self):   # 앞(front) 요소 제거
        if not self._data:
            raise IndexError('큐 비어 있음')
        return self._data.popleft()
    
    def front(self):   # 큐에서 맨앞 요소를 확인하는 메소드. 조회만 함
        if not self._data:
            raise IndexError('큐 비어 있음')
        return self._data[0]

    def is_empty(self):
        return not self._data   # 비었을 때 True 반환
    
    def size(self):
        return len(self._data)
    
    def clear(self):
        self._data.clear()

    def __repr__(self):  # front -> back 순서로 출력하는 특별 메소드
        return f'Queue(front -> back {list(self._data)})'


def demo1Func():
    imsi1 = Queue()
    imsi2 = Queue([10, 20, 30])
    print(imsi1)
    print(imsi2)
    print(imsi2.front())
    print(imsi2.size())
    imsi2.clear()
    print(imsi2)
    print('-------')
    q = Queue()
    for item in ['A','B','C','D']:
        q.enqueue(item)
        print(f'enqueue {item} -> ', q)
    
    print('FIFO에 따라 하나씩 추출')
    while not q.is_empty():
        print(f'dequeue -> ', q.dequeue(), '|now:', q)

def demo2Func(jobs, ppm=15):
    q = Queue(jobs)  # 작업들 큐에 입력
    t_sec = 0.0      # 시뮬레이션 시간 누적
    order  = []      # 실제 처리된 문서 저장

    print('프린터로 출력하기')
    while not q.is_empty():
        doc, pages = q.dequeue()
        # 출력시간 계산 : 페이지수 / 분당페이지수 * 60
        duration = (pages / ppm) * 60.0
        t_sec += duration
        order.append(doc)   # 처리 순서 기록
        print(f't={t_sec:6.1f}초 | 출력 : {doc:10s}({pages}페이지)')
    
    print('처리순서(FIFO) : ', order)

if __name__ == '__main__':
    demo1Func()
    print('문서 프린터로 출력 시뮬레이션 -FIFO')
    jobs = [('abc.pdf', 10),('nice.doc', 30),('good.txt', 5),]
    demo2Func(jobs, ppm=20)  # 현재 프린터는 1분에 20장 출력



print('==========================================================')

# 데큐(Deque) : 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조
# 놀이공원 우선 탑슨 + 일반 대기 줄

from collections import deque

dq = deque()
print('놀이공원 대기 시작')

# 일반인은 뒤쪽으로 들어옴(Queue 처럼)
dq.append('철수')
dq.append('영희')
dq.append('민수')
print('일반 대기 : ', list(dq))
print()

# VIP 고객(지수)은 앞쪽으로 들어옴
dq.appendleft('VIP지수')
print('현재 대기 줄 상태: ', list(dq))
print()

# 놀이기구에 탑승 
person = dq.popleft()
print(person, '탑승')
print('현재 대기 줄 상태2: ', list(dq))
print()

# 줄 맨 뒷사람 줄서기 포기
person = dq.pop()
print(person, ': 줄서기 포기')
print('현재 대기 줄 상태3: ', list(dq))

# 실시간 로그분석, 이동 평균 계산 등에 활용 가능
    
    


print('========================================================')

# Tree : 노드들이 나무가지 처럼 연결된 계층적 비선형 자료 구조
# 시작점이 1개이고 순환이 없다.

# 회사 조직도 구조 Tree로 표현

company = {
    'CEO':['개발팀장','기획팀장','영업팀장'],
    '개발팀장':['백엔드', '프론트엔드'],
    '기획팀장':['서비스기획'],
    '영업팀장':['국내영업','해외영업'],
    '백엔드':[],
    '프론트엔드':[],
    '서비스기획':[],
    '국내영업':[],
    '해외영업':[]
}

# 트리 구조 함수
def showTree(node, level):
    print(' ' * level + ' - ' + node)
    # 현재 노드의 자식 출력
    for child in company[node]:
        showTree(child, level + 1)  # 재귀

print('회사 조직도')
showTree('CEO', 0)



print('--------------------------------------------------------------')

# Binary Tree(이진트리) - 자식이 둘 이하(차수가 2이하)인 노드로 구성된 트리
# 노드 방문 방법 3가지 : pre-order(전위), in-order(중위), post-order(후위)
# 이진트리 순회는 DFS(깊이 우선 탐색) 기반

tree = {
    'A':('B', 'C'),
    'B':('D', 'E'),
    'C':(None, None),
    'D':(None, None),
    'E':(None, None)
}

# 전위순회
def preOrder(node):
    if node is None:
        return
    print(node, end=' ')
    left, right = tree[node]
    preOrder(left)  # 재귀
    preOrder(right)

# 중위순회
def inOrder(node):
    if node is None:
        return
    left, right = tree[node]
    inOrder(left)  # 재귀
    print(node, end=' ')
    inOrder(right)

# 후위순회
def postOrder(node):
    if node is None:
        return
    left, right = tree[node]
    postOrder(left)  # 재귀
    postOrder(right)
    print(node, end=' ')

print('전위 순회 결과 : ')
preOrder('A')
print('중위 순회 결과 : ')
inOrder('A')   # BST(Binary Search Tree) 오름차순 정렬 가능
print('후위 순회 결과 : ')
postOrder('A')