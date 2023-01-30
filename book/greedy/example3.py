M, N = map(int, input().split())
max_value = -1

for row in range(N):
    data = list(map(int, input().split()))
    min_data = min(data)
    max(max_value, min_data)

print(max_value)
