N = int(input())
orders = map(str, input().split())

point = [1, 1]

for order in orders:
    if order == "L" and point[1] > 1:
        point[1] -= 1
    elif order == "R" and point[1] < N:
        point[1] += 1
    elif order == "U" and point[0] > 1:
        point[0] -= 1
    elif order == "D" and point[0] < N:
        point[0] += 1

print(point)
