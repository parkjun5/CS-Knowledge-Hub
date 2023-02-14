from collections import deque

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input())))

exp = 1

queue = deque()


def adventure():
    # do somthing
    queue.append([0, 0])

    while queue:
        now = queue.popleft()
        now_minus_x = now[0] - 1
        now_minus_y = now[1] - 1
        now_plus_x = now[0] + 1
        now_plus_y = now[1] + 1

        now_value = maps[now[0]][now[1]]

        if now_minus_x >= 0 and maps[now_minus_x][now[1]] == 1:
            queue.append([now_minus_x, now[1]])
            maps[now_minus_x][now[1]] = now_value + 1
        if now_plus_x < n and maps[now_plus_x][now[1]] == 1:
            queue.append([now_plus_x, now[1]])
            maps[now_plus_x][now[1]] = now_value + 1
        if now_minus_y >= 0 and maps[now[0]][now_minus_y] == 1:
            queue.append([now[0], now_minus_y])
            maps[now[0]][now_minus_y] = now_value + 1
        if now_plus_y < m and maps[now[0]][now_plus_y] == 1:
            queue.append([now[0], now_plus_y])
            maps[now[0]][now_plus_y] = now_value + 1


adventure()

print(maps)
print(maps[n-1][m-1])
