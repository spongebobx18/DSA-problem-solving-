def solve(n,nums):
    nums.sort()
    l,r = 0,n-1
    res =0
    while l<r:
        res+=(nums[r]-nums[l])
        l+=1
        r-=1
    print(res)
        


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    solve(n,arr)