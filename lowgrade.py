if __name__ == '__main__':
    
    n = int(input())
    
    s_list = []
    
    for _ in range(n):
        name = input()
        grade = float(input())
        s_list.append([name, grade])
    
    grades = set([student[1] for student in s_list])
    second_lowest_grade = sorted(grades)[1]
    
    lowest_grade = [student[0] for student in s_list if student[1] == second_lowest_grade]
    
    lowest_grade.sort()
    
    
    for name in lowest_grade:
        print(name)
