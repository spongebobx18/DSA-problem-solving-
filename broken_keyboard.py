def solve():
    s = str(input())
    result = set()
    left = 0
    while left < len(s):
        if left+1 >= len(s) or s[left] != s[left+1]:
            result.add(s[left])
            left += 1
        else:
            left += 2
    print("".join(sorted(list(result))))
t = int(input())
for _ in range(t):
    solve()