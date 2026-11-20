# bst
# 중위 순회로 자료 정렬하기
# 각 노드 기준으로 left < node < right
# 왼쪽 서브트리 : 현재 노드보다 작은 값
# 오른쪽 서브트리 : 현재 노드보다 큰 값
# 입력 순성에 따라 트리 모양이 달라짐
# 이진트리는 구조만 있으나, BST 구조 + 정렬규칙이 있다.
# 중위순회를 하면 오름차순 정렬됨

# BST 노드 정의 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# BST에 자료 삽입
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.key)
    inorder(root.right, result)

values = [5, 3, 7, 2, 4, 9]
root = None
for v in values:
    root = insert(root, v)

# BST 정렬 결과 출력
sorted_result = []
inorder(root, sorted_result)
print('순회 결과 : ', sorted_result)