def icecream(graph, x, y, visited, stack):
    if x > 4 or y > 3:
        return
    if not visited[y][x]:
        if graph[y][x] == 0:
            visited[y][x] = True
            stack.append([y, x])
            icecream(graph, x + 1, y, visited)
            icecream(graph, x, y + 1, visited)
        else:
            visited[y][x] = True
            icecream(graph, x + 1, y, visited)
            icecream(graph, x, y + 1, visited)


graph = []

n, m = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]
count = 0
stack = []
icecream(graph, 0, 0, visited, stack)

while stack:
    pop_value = stack.pop()
    # 0, 0
    stack