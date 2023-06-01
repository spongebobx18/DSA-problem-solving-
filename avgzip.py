


marks, students = tuple(map(int,input().split()))

total = []
for _ in range(students):
    marks = list(map(float, input().split()))
    total.append(marks)
    
averages = [sum(marks)/students for marks in zip(*total)]
    
for average in averages:
    print(average)
    
    

    
    
        