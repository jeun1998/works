# graph : node(vertex)와 edge의 집합으로 이루어진 자료구조
# tree : 계층구조, root있음, 사이클 없음, 항상 연결
# graph : 일반 네트워크 구조, root 없음, 사이클 있음, 연결/비연결 모두 가능

graph = {
    'A':('B', 'C'),
    'B':('D', 'E'),
    'C':('F'),
    'D':(),
    'E':(),
    'F':()
}

# DFS : 깊이 우선 탐색 방식 - 재귀 또는 스텍으로 구현 - 경로 추적, 백트래킹에 적합
visited_dfs = []

def dfsFunc(graph, start, visited):
    visited_dfs.append(start)
    for next_node in graph[start]:     # 이웃 노드 탐색 : 현재 노드에 인접한 노드를 하나
        if next_node not in visited:
            dfsFunc(graph, next_node, visited)

dfsFunc(graph, 'A', visited_dfs)
print('DFS 방문 순서 : ', visited_dfs)
print()
from collections import deque
def bfsFunc(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return visited

visited_dfs = bfsFunc(graph, 'A')
print('BFS 방문 순서 : ', visited_dfs)
