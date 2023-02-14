from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        pop_value = queue.popleft()
        print(pop_value, end=" ")

        for index in graph[pop_value]:
            if not visited[index]:
                visited[index] = True
                queue.append(index)


    # for i in graph[start]:
    #     if not visited[i]:
    #         visited[i] = True
    #         queue.append(i)
    #
    # for index in graph[start]:
    #     pop_value = queue.popleft()
    #     bfs(graph, pop_value, visited)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

bfs(graph, 1, visited)
