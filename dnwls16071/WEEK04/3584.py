import sys
input = sys.stdin.readline
from collections import deque

def BFS(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                depth[i] = depth[v] + 1
                parent[i] = v
                q.append(i)
                
def LCA(a, b):
    a_ancestor = [a]    # a를 포함한 a의 모든 조상 노드들
    b_ancestor = [b]    # b를 포함한 b의 모든 조상 노드들
    
    while parent[a] != a:
        a_ancestor.append(parent[a])
        a = parent[a]
    while parent[b] != b:
        b_ancestor.append(parent[b])
        b = parent[b]
    
    idx_a = len(a_ancestor)-1; idx_b = len(b_ancestor)-1
    while a_ancestor[idx_a] == b_ancestor[idx_b]:
        idx_a -= 1
        idx_b -= 1
    return a_ancestor[idx_a + 1]
        
T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N + 1)]
    depth = [0] * (N + 1)
    visited = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        # a가 b의 부모
        a, b = map(int, input().split())
        parent[b] = a
    c, d = map(int, input().split())
    BFS(1)
    print(LCA(c, d))