n = int(input()) 
points = list(map(int, input().split()))  
amazing_performances = 0  
min_points = max_points = points[0] 

for i in range(1, n):
    if points[i] < min_points:
        min_points = points[i]
        amazing_performances += 1
    elif points[i] > max_points:
        max_points = points[i]
        amazing_performances += 1

print(amazing_performances)
