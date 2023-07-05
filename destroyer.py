from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = Counter(a)
    
    found = False

    for i in range(max(b)):
        if b[i+1] > b[i] or i+1 not in b:
            found = True
            break
    
    if found:
        print("NO")
    else:
        print("YES")


"""
Time: O(N)
"""