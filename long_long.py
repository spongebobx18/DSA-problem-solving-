t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    operations = 0
    while i < n:
        if a[i] < 0:
            operations += 1
            while i < n and a[i] <= 0:
                a[i] = a[i]*-1
                i+= 1
        
        i+= 1
            
    print(sum(a),operations)