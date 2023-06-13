N, M = map(int, input().split())
x, y, direction = map(int, input().split())

record = [[0] * M for _ in range(N)]
record[x][y] = 1
count = 1

maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))

# 북 동 남 서
direction_x = [0, -1, 0, 1]
direction_y = [1, 0, -1, 0]

direction_count = 0


# def is_behind_sea():
#     global from_x, from_y
#     from_x = x - direction_x[direction]
#     from_y = y - direction_y[direction]
#     return maps[from_x][from_y] == 1


def turn_left():
    global direction
    direction -= 1

    if direction == -1:
        direction = 3


while True:
    if direction_count == 4:
        from_x = x - direction_x[direction]
        from_y = y - direction_y[direction]
        if maps[from_x][from_y] == 1:
            break

        x = from_x
        y = from_y
        direction_count = 0
        break

    turn_left()
    direction_count += 1

    to_x = x + direction_x[direction]
    to_y = y + direction_y[direction]

    if maps[to_x][to_y] == 0 and record[to_x][to_y] == 0:
        direction_count = 0
        record[to_x][to_y] = 1
        x = to_x
        y = to_y
        count += 1

print(count)
