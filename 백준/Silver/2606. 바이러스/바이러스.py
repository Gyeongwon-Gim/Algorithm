from collections import deque
# 바이러스 - BFS
com = int(input())
link = int(input())

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    cnt = 0
    # 현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑는다
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

if __name__ == "__main__":
    # 그래프 입력 받기
    # 0번째는 사용하지 않는다.
    graph = [[] for _ in range(com + 1)]
    for _ in range(link):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (com + 1)

    print(bfs(graph, 1, visited))