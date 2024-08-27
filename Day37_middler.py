# 99club Day37_middler - 2024-08-27(Tue)
# https://www.acmicpc.net/problem/2529

from collections import defaultdict, deque

def bfs(graph, start):
    visited = [start]
    q = deque([start])
    n = 1

    while q:
        node = q.popleft()

        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                q.append(adjacent)
                n += 1

    return n


def solution(n, wires):
    answer = -1


    arr = []

    for i in wires:
        graph = defaultdict(list)
        x, y = i
        for j in wires:
            if i == j:
                continue
            a, b = j
            graph[a].append(b)
            graph[b].append(a)

        n1 = bfs(graph, x)
        n2 = bfs(graph, y)

        arr.append(abs(n1 - n2))

    answer = min(arr)

    return answer
