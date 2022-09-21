from collections import deque

def course(n, pre_req):
    graph = [[] for i in range(n)]
    indegrees = [0 for i in range(n)]
    for req in pre_req:
        graph[req[0]].append(req[1])
        indegrees[req[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegrees[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighboor in graph[vertex]:
            indegrees[neighboor] -= 1
            if indegrees[neighboor] == 0:
                queue.append(neighboor)
    return len(order) == n
