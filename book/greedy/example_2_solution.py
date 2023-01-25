n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

## sol 1
# k_first = k * first
# seq_sum_val = (m // k) * (k_first + second)
# last = m % k_first
#
# result = seq_sum_val + last

## sol2

first_count = int(m / (k + 1)) * k
first_count += m % (k + 1)

result = first_count * first
result += (m - first_count) * second

print(result)
