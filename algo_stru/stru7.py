# 에이스타 알고리즘은 출발 노드에서 목표 노드까지의 최단 경로를
# 빠르게 찾는 그래프 탐색 알고리즘

# 동작 방식
# 1. 출발 노드를 열린 목록에 넣고 시작
# 2. 열린 목록에서 f(n) 값이 가장 작은 노드를 선택
# 3. 해당 노드가 목표 노드면 탐색을 종료하고 경로 반환
# 4. 목표가 아니면 현재 노드를 닫힌 목록으로 옮기고,
# 인접 이동 가능 노드의 g, h, f 값을 계산해 열린 목록에 추가하거나 갱신
# 5. 목표에 도달하거나 열린 목록이 빌 때까지 2~4단계 반복한다
import heapq

def astarFunc(graph, start, goal, h):
    pq = [(h[start], 0, start)]
    dist = {start:0}
    parent = {}
    while pq:
        f, g, u = heapq.heappush(pq)
        if u == goal:
            break
        for v, w in graph[u]:  
            new_g = g + w
            if v not in dist or new_g < dist[v]:
                dist[v] = new_g
                parent[v] = u
                heapq.heappush(pq, (new_g + h[v], new_g, v))

        path = [goal]
        while path[-1] != start:
            path.append(parent[path[-1]])
            path.reverse()
            return path, dist[goal]

graph = {
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',1),('D',2)],
    'C':[('A',4),('B',1),('D',3)],
    'D':[('B',2),('C',3)]
}

heuristic = {'A':3, 'B':2, 'C':1, 'D':0}
astarFunc(graph, 'A', 'D', heuristic)