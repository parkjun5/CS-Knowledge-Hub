input_str = input()
x = ord(input_str[0])
y = int(input_str[1])

result = 0
plus_x_1_list = [2, 2, -2, -2]
plus_y_2_list = [1, -1, -1, 1]

plus_x_2_list = [1, 1, -1, -1]
plus_y_1_list = [2, -2, -2, 2]

# 네 방향 확인  x  최소 97 최대 104
for index in range(4):
    x_1 = x + plus_x_1_list[index]
    y_2 = y + plus_y_2_list[index]

    x_2 = x + plus_x_2_list[index]
    y_1 = y + plus_y_1_list[index]
    if 96 < x_1 < 105 and 0 < y_2 < 9:
        result += 1
    if 96 < x_2 < 105 and 0 < y_1 < 9:
        result += 1

print(result)
