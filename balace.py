def max_balanced_team(n, skills):
    skills.sort()  # Sort the skills in ascending order.
    max_students = 1  # The minimum possible team size is 1 (one student).

    left, right = 0, 1
    while right < n:
        if skills[right] - skills[left] <= 5:
            max_students = max(max_students, right - left + 1)
            right += 1
        else:
            left += 1

    return max_students

# Input
n = int(input())
skills = list(map(int, input().split()))

# Output
result = max_balanced_team(n, skills)
print(result)