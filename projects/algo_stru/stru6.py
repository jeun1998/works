# 다익스트라 알고리즘
# 그래프는 dict로 표현
# 우선순위 큐를 이용해 이동 비용이 적은 도시부터 탐색
# 기존 경로보다 짧은 경로를 발견하면 거리 갱신

import heapq
INF = float('inf')

graph = {
    '서울':[('대전',2),('대구',5),('인천',1)],
    '대전':[('서울',2),('대구',3),('인천',2)],
    '대구':[('서울',5),('대전',3),('인천',3),('광주',1),('부산',5)],
    '인천':[('서울',1),('대전',2),('대구',3),('광주',1)],
    '광주':[('대구',1),('인천',1),('부산',2)],
    '부산':[('대구',5),('광주',2)]
}

def dijkstraFunc(start):
    distance = {city:INF for city in graph}

    previous = {city:None for city in graph}

    pq = []
    distance[start] = 0

    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next_city, cost in graph[now]:

            new_cost = dist + cost
            if new_cost < distance[next_city]:
                distance[next_city] = new_cost

                previous[next_city] = now
                heapq.heappush(pq, (new_cost, next_city))
    return distance, previous

def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

start_city = '서울'
distance, previous = dijkstraFunc(start_city)
print(f'\n{start_city} 출발 최단 경로')
for city in graph:
    path = get_path(previous, start_city, city)
    if distance[city] == INF:
        print(f'{start_city} -> {city} : 이동 불가')
        continue

    route = ' -> '.join(path)

    print(f'도착지 : {city}, 최단 비용 : {distance[city]}')
    print(f'이동 경로 : {route}')
    print('-' * 30)
