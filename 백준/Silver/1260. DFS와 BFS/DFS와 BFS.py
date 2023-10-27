from collections import deque

def dfs(graph: list, v: int, visited: list) -> None:
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph: list, start: int, visited:list) -> None:
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    visited = [False for _ in range(N + 1)]
    # 그래프 입력 받기 (0번째 노드 없음)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    graph = [sorted(i) for i in graph]
    
    dfs(graph, V, visited)
    visited = [False for _ in range(N + 1)]
    print()
    bfs(graph, V, visited)