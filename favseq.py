t = int(input())
cases = []

for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    cases.append((n, b))

a = []
for n,b in cases:
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            a.append(b[left])
        else:
            a.append(b[left])
            a.append(b[right])
        left += 1
        right -= 1
print(a)
