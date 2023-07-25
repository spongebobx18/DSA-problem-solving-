
count = 0
all_pairs = []
n=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    for j in range(i + 1,n):
        all_pairs.append((a[i] + a[j], b[i] + b[j]))

for pair in all_pairs:
    if pair[0] > pair[1]:
        count += 1
print(count)
