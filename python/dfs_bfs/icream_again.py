n, m = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

print(n, m)
print(maps)


def bfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if maps[x][y] == 0:
        maps[x][y] = 1
        bfs(x - 1, y)
        bfs(x, y - 1)
        bfs(x + 1, y)
        bfs(x, y + 1)
        return True
    else:
        False

result = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j):
            result += 1


print(result)
