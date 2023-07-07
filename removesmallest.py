def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        found = True

        for i in range(1, n):
            if nums[i] - nums[i-1] > 1:
                results.append("NO")
                found = False
                break

        if found:
            results.append("YES")

    for result in results:   #in order to print all the results after the inputs , you have to append them in the results 
        print(result)

solve()
