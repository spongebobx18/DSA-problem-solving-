def cube():
    n = int(input())
    line = list(map(int, input().split()))
    
    for i in range(1,n):
        if line[i] >= line[i-1]:
            return False
    return True

for i in range(int(input())):
    if cube()==True:
        print("NO")
    else:
        print("YES")