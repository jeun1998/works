# Dijkstra 알고리즘
# 가중치가 있는 그래프에서 한 시작점으로 붙 모든 정점까지의 최단 거리 구하는 알고리즘
# 조건 : 간선 가중치는 음수가 없어야 함. 그래프에는 여러경로가 있을 수 있음
# 우선 순위큐를 사용
# 작동 방식
# 1) 출발 노드를 설정
# 2) 출발 노드를 기준으로 각 노드의 최소 비용 저장
# 3) 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
# 4) 해당 노드를 거쳐서 특정한 노드로 가는 경우 고려하여 최소 비용 갱신
# 5) 더 이상의 최소 노드가 없을 때까지 위 과정에서 3번 4번 반복
import heapq
graph = {
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',1),('D',2)],
    'C':[('A',4),('B',1),('D',3)],
    'D':[('B',2),('C',3)]
}

def dijkstraFunc(graph, start):
    dist = {node:float('inf') for node in graph}
    dist[start] = 0
    print(dist)
    pq = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

print(dijkstraFunc(graph, 'A'))