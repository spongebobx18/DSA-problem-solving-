n = int(input())
sequence = list(map(int, input().split()))

total_sum = sum(sequence)
indices = []

for i in range(n):
    if (total_sum - sequence[i]) == (n - 1) * sequence[i]:
        indices.append(i + 1)

count = len(indices)
print(count)
if count > 0:
    print(" ".join(map(str, indices)))
