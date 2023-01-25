n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse=True)


def same_case(target, num):
    for i in range(0, m):
        target += num
    return target


def diff_case(target, num1, num2, k):
    count = 0
    for i in range(0, m):
        count += 1
        if count == k:
            target += num2
            count = 0
        else:
            target += num1

    return target


if data[0] == data[1]:
    result = same_case(result, data[0])
else:
    result = diff_case(result, data[0], data[1], k)

print(result)
